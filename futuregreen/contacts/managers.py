# contacts/managers.py

from django.db import models
from django.db.models.query import QuerySet

class ContactMixin(object):
    def people(self):
        return self.get_query_set().filter(contact_type=self.model.TYPE_PERSON)

    def organizations(self):
        return self.get_query_set().exclude(contact_type=self.model.TYPE_PERSON)

class ContactQuerySet(QuerySet, ContactMixin):
    pass

class ContactManager(models.Manager, ContactMixin):
    def get_query_set(self):
        return ContactQuerySet(self.model, using=self._db)

