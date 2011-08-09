# futuregreen/studio/models.py

from django.db import models

from taggit.managers import TaggableManager
from contacts.models import ContactBase

class EmployeeType(models.Model):
    name =  models.CharField(max_length=255)
    description = models.TextField(blank=True)

    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from name. Must be unique.")

    def __unicode__(self):
        return u'%s' % self.name

class Contact(ContactBase):
    # taxonomy
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True

class Client(Contact):
    pass

class Collaborator(Contact):
    pass

class Employee(Contact):
    # employee status choices
    STATUS_FULL = 1
    STATUS_CONTRACT = 2
    STATUS_FORMER = 3
    STATUS_CHOICES = (
        (STATUS_FULL, 'Full-time'),
        (STATUS_CONTRACT, 'Contract'),
        (STATUS_FORMER, 'Former'),
    )

    # extended core fields
    employee_type = models.ForeignKey(EmployeeType)
    job_title = models.CharField(max_length=250)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
                                              default=STATUS_FULL)

