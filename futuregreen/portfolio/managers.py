# portfolio/managers.py

from datetime import datetime

from django.db import models
from django.db.models.query import QuerySet

class ProjectMixin(object):
    def live(self):
        return self.get_query_set().filter(status=self.model.STATUS_LIVE)

    def stage(self):
        return self.get_query_set().exclude(status=self.model.STATUS_DRAFT)\
                                   .exclude(status=self.model.STATUS_HIDDEN)
    def featured(self):
        return self.get_query_set().filter(status=self.model.STATUS_LIVE)\
                                   .filter(featured=True)
    def current(self):
        return self.get_query_set().filter(status=self.model.STATUS_LIVE)\
                                   .filter(date_start__gte=datetime.now)

    def completed(self):
        return self.get_query_set().filter(status=self.model.STATUS_LIVE)\
                                   .filter(date_end__lte=datetime.now)

    def future(self):
        return self.get_query_set().filter(status=self.model.STATUS_LIVE)\
                                   .filter(date_start__lte=datetime.now)

    def size_asc(self):
        return self.get_query_set().filter(status=self.model.STATUS_LIVE)\
                                   .order_by('area_normalized')

    def size_desc(self):
        return self.get_query_set().filter(status=self.model.STATUS_LIVE)\
                                   .order_by('-area_normalized')

class ProjectQuerySet(QuerySet, ProjectMixin):
    pass

class ProjectManager(models.Manager, ProjectMixin):
    def get_query_set(self):
        return ProjectQuerySet(self.model, using=self._db)