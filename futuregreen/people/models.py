# studio/models.py

from django.db import models
from django.auth.models import User

from contacts.models import ContactBase
from images.models import ImageFieldAutoMixin

class Contact(ContactBase):
    pass

class Client(Contact):
    def set_relation(self):
        self.relation = 'client'

    class meta:
        proxy = True

class Collaborator(Contact):
    def set_relation(self):
        self.relation = 'collaborator'

    class meta:
        proxy = True

class EmployeeType(models.Model):
    name =  models.CharField(max_length=255)
    description = models.TextField(blank=True)

    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from name. Must be unique.")

    def __unicode__(self):
        return u'%s' % self.name

class Employee(ImageFieldAutoMixin, Contact):
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

    user = models.ForeignKey(User, blank=True)

    def save(self, force_insert=False, force_update=False):
        self.contact_type = self.TYPE_PERSON
        super(Employee, self).save(force_insert, force_update)