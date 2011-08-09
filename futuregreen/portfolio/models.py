# futuregreen/portfolio/models.py

from django.db import models

from taggit import TaggableManager

from projects.models import PhysicalProjectBase

from futuregreen.studio.models import Client, Collaborator, Employee

class Project(PhysicalProjectBase):
    """FutureGreen project. Extends projects.PhysicalProjectBase
    """

    # relations
    designers = models.ManyToManyField(Employee, blank=True, null=True)
    clients = models.ManyToManyField(Client, blank=True, null=True)
    collaborators = models.ManyToManyField(Collaborator, blank=True, null=True)

    # taxonomy
    tags = TaggableManager()


