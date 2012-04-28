# portfolio/managers.py

from datetime import datetime

from django.db import models
from django.db.models.query import QuerySet

class ImageMixin(object):
    def public(self):
        return self.get_query_set().filter(public=True)

class ImageQuerySet(QuerySet, ImageMixin):
    pass

class ImageManager(models.Manager, ImageMixin):
    def get_query_set(self):
        return ImageQuerySet(self.model, using=self._db)