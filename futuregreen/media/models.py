#coding: utf-8
# media/models.py
"""

    A pluggable media management app for django.

    Borrows from django-generic-images:
    https://bitbucket.org/kmike/django-generic-images/
    by https://bitbucket.org/kmike/

"""
import os

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.files.storage import default_storage
from django.db import models
from django.db.models import Max


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

class ReplaceOldImageMixin(models.Model):
    """
        If the file for image is re-uploaded, old file is deleted.

    """

    def _replace_old_image(self):
        """ Override this in subclass if you don't want
            image replacing or want to customize image replacing
        """
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
    
    #objects = ImageManager()

    # core fields
    name = models.CharField(max_length=255)
    caption = models.TextField(null=True, blank=True)

    # relations
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        abstract=True

    def __unicode__(self):
        return u'%s' % self.name


class RelatedImageBase(ImageBase):
    """
        An abstract image to be associated with another content object

    """
    # metadata
    is_main = models.BooleanField('Main image', default=False)
    order = models.IntegerField(default=0)

    def _get_next_pk(self):
        max_pk = self.__class__.objects.aggregate(m=Max('pk'))['m'] or 0
        return max_pk+1

    def save(self, *args, **kwargs):
        if self.is_main:
            related_images = self.__class__.objects.filter(
                                                content_type=self.content_type,
                                                object_id=self.object_id
                                            )
            related_images.update(is_main=False)

        if not self.pk: # object is created
            if not self.order: # order is not set
                self.order = self._get_next_pk() # let it be max(pk)+1

        super(RelatedImageBase, self).save(*args, **kwargs)

    class Meta:
        abstract=True



class GenericRelatedImageBase(ImageBase):
    """
        An image that can be attached to any other content object

    """

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    # metadata
    is_main = models.BooleanField('Main image', default=False)
    order = models.IntegerField(default=0)

    def get_upload_path(self, filename):
        """ Override this in proxy subclass to customize upload path..
        """
        related_object = str(self.content_object) if self.content_object else 'common'

        root, ext = os.path.splitext(filename)
        return os.path.join('images', related_object,
                            self.filename + ext)

    def next(self):
        """ Returns next image for same content_object and None if image is
        the last. """
        try:
            return self.__class__.objects.for_model(self.content_object,
                                                    self.content_type).\
                            filter(order__lt=self.order).order_by('-order')[0]
        except IndexError:
            return None

    def previous(self):
        """ Returns previous image for same content_object and None if image
        is the first. """
        try:
            return self.__class__.objects.for_model(self.content_object,
                                                    self.content_type).\
                            filter(order__gt=self.order).order_by('order')[0]
        except IndexError:
            return None

    def get_order_in_album(self, reversed_ordering=True):
        """ Returns image order number. It is calculated as (number+1) of images
        attached to the same content_object whose order is greater
        (if 'reverse_ordering' is True) or lesser (if 'reverse_ordering' is
        False) than image's order.
        """
        lookup = 'order__gt' if reversed_ordering else 'order__lt'
        return self.__class__.objects.\
                        for_model(self.content_object, self.content_type).\
                        filter(**{lookup: self.order}).count() + 1


    def _get_next_pk(self):
        max_pk = self.__class__.objects.aggregate(m=Max('pk'))['m'] or 0
        return max_pk+1

    def save(self, *args, **kwargs):
        if self.is_main:
            related_images = self.__class__.objects.filter(
                                                content_type=self.content_type,
                                                object_id=self.object_id
                                            )
            related_images.update(is_main=False)

        if not self.pk: # object is created
            if not self.order: # order is not set
                self.order = self._get_next_pk() # let it be max(pk)+1

        super(GenericRelatedImageBase, self).save(*args, **kwargs)

    class Meta:
        abstract=True