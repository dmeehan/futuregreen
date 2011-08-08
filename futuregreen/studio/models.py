# futuregreen/studio/models.py

from django.db import models

from taggit import TaggableManager
from contacts.models import ContactBase

class EmployeeType(models.Model):
    name =  models.CharField(max_length=255)
    description = models.TextField(blank=True)

    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from name. Must be unique.")

class Contact(ContactBase):
    tags = TaggableManager()

    class Meta:
        abstract = True

class Client(Contact):
    pass

class Collaborator(Contact):
    pass

class Employee(Contact):
    employee_type = models.ForeignKey(EmployeeType)
    title = models.CharField(max_length=250)

