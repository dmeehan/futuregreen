# coding: utf-8
# images/models.py
"""

    A pluggable image management app for django.
    Requires django-imagekit and PIL.

    Borrows from django-generic-images:
    https://bitbucket.org/kmike/django-generic-images/
    by https://bitbucket.org/kmike/

"""
import os

from django.conf import settings
from django.db import models, transaction

from imagekit.models import ImageModel

from futuregreen.images.fields import PositionField

class ImageFieldMixin(models.Model):
    """
        Simple abstract Model class mixin that supplies an image field.

    """

    def get_upload_path(self, filename):
        name = self.__class__.__name__
        model = name.lower()
        return os.path.join('images', model, filename)

    def _upload_path_wrapper(self, filename):
        return self.get_upload_path(filename)

    image = models.ImageField(upload_to=_upload_path_wrapper, blank=True, null=True)

    class Meta:
        abstract = True

class ImageFieldAutoMixin(ImageModel, ImageFieldMixin):
    """
        Simple abstract Model class mixin that supplies an image field and includes
        specs for image resizing and processing via Imagekit. Imagekit options must be
        defined in the projects settings file.

    """
    CROPHORZ_LEFT = 0
    CROPHORZ_CENTER = 1
    CROPHORZ_RIGHT = 2
    CROPHORZ_CHOICES = (
        (CROPHORZ_LEFT, 'left'),
        (CROPHORZ_CENTER, 'center'),
        (CROPHORZ_RIGHT, 'right'),
    )

    CROPVERT_TOP = 0
    CROPVERT_CENTER = 1
    CROPVERT_BOTTOM = 2
    CROPVERT_CHOICES = (
        (CROPVERT_TOP, 'top'),
        (CROPVERT_CENTER, 'center'),
        (CROPVERT_BOTTOM, 'bottom'),
    )

    crop_horz = models.PositiveSmallIntegerField(
                    verbose_name='crop image horizontally',
                    choices=CROPHORZ_CHOICES,
                    blank=True,
                    default=CROPHORZ_CENTER,
                    help_text="From where to horizontally crop the image, if cropping is necessary.")

    crop_vert = models.PositiveSmallIntegerField(
                    verbose_name='crop image vertically',
                    choices=CROPVERT_CHOICES,
                    blank=True,
                    default=CROPVERT_CENTER,
                    help_text="From were to vertically crop the image, if cropping is necessary.")
    
    class Meta:
        abstract = True

    class IKOptions:
        spec_module = settings.IMAGES_SPEC_FILE
        cache_dir = settings.IMAGES_CACHE_DIR
        cache_filename_format = settings.IMAGES_CACHE_FILENAME_FORMAT
        preprocessor_spec = settings.IMAGES_PREPROCESSOR_SPEC

class ReplaceOldImageMixin(models.Model):
    """
        If the file for image is re-uploaded, old file is deleted.

    """

    def _replace_old_image(self):
        try:
            old_obj = self.__class__.objects.get(pk=self.pk)
            if old_obj.image.path != self.image.path:
                path = old_obj.image.path
                default_storage.delete(path)
        except self.__class__.DoesNotExist:
            pass

    def save(self, *args, **kwargs):
        if self.pk:
            self._replace_old_image()
        super(ReplaceOldImageMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class ImageBase(models.Model):
    """
        Abstract Image model fields.

    """

    # core fields
    name = models.CharField(max_length=255, blank=True)
    caption = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=True, help_text="This file is publicly available.")

    class Meta:
        abstract=True

    def __unicode__(self):
        return u'%s' % self.name


class ImageAutoBase(ImageFieldAutoMixin, ImageBase):
    """
        Abstract Image model that will be automatically
        re-sized and processed based on the project image specs.

    """

    class Meta:
        abstract=True


class RelatedImageAutoBase(ImageAutoBase):
    """
        An subclass of ImageAutoBase that adds fields and
        methods to define an image collection attached to a
        related model. To use in a project, subclass this model
        and add a foreign key field to the related model you wish to
        have an image collection.

    """
    
    def _get_fk_field_name(self):
        """ This looks for a foreign key field on the model. If there is one,
            it uses this field to order the image collection. There can only be one foreign key
            field for each image model. If there is more than one, you must override this method in
            your sub class to define the proper foreign key explicitly.
            i.e. fk_field_name = <your selected foreign key field name>
        """
        opts = self._meta
        fk_field_list = [f for f in opts.fields if f.get_internal_type() == "ForeignKey"]
        try:
            if len(fk_field_list) == 1:
                fk_field_name = [f.name for f in fk_field_list][0]
                return fk_field_name
        except:
            raise NotImplementedError

    order = PositionField(unique_for_field=_get_fk_field_name)
    is_main = models.BooleanField('Main image', default=False)

    class Meta:
        abstract=True
        ordering = ['order']

    def get_upload_path(self, filename):
        related_model = self._get_fk_field_name()
        return os.path.join('images', related_model, filename)

    def save(self, *args, **kwargs):
        if self.is_main:
            kwargs = {self._get_fk_field_name(): getattr(self, self._get_fk_field_name())}
            related_images = self._default_manager.filter(**kwargs)
            related_images.update(is_main=False)
            kwargs = {}

        super(RelatedImageAutoBase, self).save(*args, **kwargs)
