# coding: utf-8
# media/models.py
"""

    A pluggable media management app for django.

    Borrows from django-generic-images:
    https://bitbucket.org/kmike/django-generic-images/
    by https://bitbucket.org/kmike/

"""
from django.conf import settings
from django.db import models
from imagekit import ImageModel

from media.fields import PositionField

class ImageFieldMixin(models.Model):
    """
        Simple abstract Model class with image field.

    """

    def get_upload_path(self, filename):
        """ Override this to customize upload path """
        raise NotImplementedError

    def _upload_path_wrapper(self, filename):
        return self.get_upload_path(filename)

    image = models.ImageField(upload_to=_upload_path_wrapper)

    class Meta:
        abstract = True

class ImageFieldAutoSizeMixin(ImageModel, ImageFieldMixin):
    """
        Simple abstract Model class with image field that includes
        resize specs.

    """
    class Meta:
        abstract = True

    class IKOptions:
        spec_module = '%s.imagespecs' % settings.PROJECT_DIR
        cache_dir = 'resized'

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


class ImageBase(ImageFieldMixin):
    """
        Abstract Image model.
         
    """

    # core fields
    name = models.CharField(max_length=255)
    caption = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=True, help_text="This file is publicly available.")

    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from name. Must be unique.")

    class Meta:
        abstract=True

    def __unicode__(self):
        return u'%s' % self.name


class ImageAutoSizeBase(ImageBase, ImageModel):
    """
        Abstract Image model that will be automatically
        resized based on the project image specs.

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
                    verbose_name='horizontal cropping',
                    choices=CROPHORZ_CHOICES,
                    blank=True,
                    default=CROPHORZ_CENTER,
                    help_text="From where to horizontally crop the image, if cropping is necessary.")

    crop_vert = models.PositiveSmallIntegerField(
                    verbose_name='vertical cropping',
                    choices=CROPVERT_CHOICES,
                    blank=True,
                    default=CROPVERT_CENTER,
                    help_text="From were to vertically crop the image, if cropping is necessary.")
    
    class Meta:
        abstract=True
        
    class IKOptions:
        spec_module = settings.MEDIA_SPEC_FILE
        cache_dir = 'resized'


class RelatedImageAutoSizeBase(ImageAutoSizeBase):
    """
        Abstract Image model that will be automatically
        resized based on the project image specs. Includes a
        property to manually define the images related field
        in a subclass.

    """
    @property
    def fk_field(self):
        """ This looks for a foreign key field on the model. If there is one,
            it uses this field to order the image collection. There can only be one foreign key
            field for each image model. If there is more than one, override this field in
            your sub class to define the proper foreign key explicitly.
        """
        opts = self._meta
        fk_field = [f for f in opts.fields if f.get_internal_type() == "ForeignKey"][0]
        return fk_field

    order = PositionField(unique_for_field=fk_field.name)
    is_main = models.BooleanField('Main image', default=False)

    class Meta:
        ordering = ['order',]

    def get_upload_path(self, filename):
        return os.path.join('images', self.fk_field.name, filename)

    def save(self, *args, **kwargs):
        if self.is_main:
            related_images = self._default_manager.filter(
                self.fk_field.name = self.)
            related_images.update(is_main=False)

        super(RelatedImageAutoSizeBase, self).save(*args, **kwargs)

    class Meta:
        abstract=True


class GenericRelatedImageAutoSizeBase(RelatedImageAutoSizeBase):
    """
        Abstract Image model that will be automatically
        resized based on the project image specs. Includes a
        property to manually define the images related field
        in a subclass.

    """

    def get_upload_path(self, filename):
        return os.path.join('images', self.related_field, filename)

    def save(self, *args, **kwargs):
        if self.is_main:
            related_images = self._default_manager.filter(
                project=self.related_field)
            related_images.update(is_main=False)

        super(ProjectImage, self).save(*args, **kwargs)

    class Meta:
        abstract=True