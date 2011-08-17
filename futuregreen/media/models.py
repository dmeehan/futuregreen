#coding: utf-8
# media/models.py
"""

    A pluggable media management app for django.

    Borrows from django-generic-images:
    https://bitbucket.org/kmike/django-generic-images/
    by https://bitbucket.org/kmike/

"""

from django.db import models


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

    # core fields
    name = models.CharField(max_length=255)
    caption = models.TextField(null=True, blank=True)

    class Meta:
        abstract=True

    def __unicode__(self):
        return u'%s' % self.name