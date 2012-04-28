# blocks/managers.py

from datetime import datetime

from django.db import models
from django.db.models.query import QuerySet

class PostMixin(object):
    def live(self):
        return self.get_query_set().filter(status=self.model.STATUS_LIVE)

    def featured(self):
        return self.get_query_set().filter(status=self.model.STATUS_LIVE)\
                                   .filter(featured=True)
    def future(self):
        return self.get_query_set().filter(status=self.model.STATUS_LIVE)\
                                   .filter(date_published__lte=datetime.now)

class PostQuerySet(QuerySet, PostMixin):
    pass

class PostManager(models.Manager, PostMixin):
    def get_query_set(self):
        return PostQuerySet(self.model, using=self._db)