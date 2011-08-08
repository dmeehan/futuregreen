# futuregreen/portfolio/models.py

from django.db import models

from taggit import TaggableManager

from projects.models import PhysicalProjectBase

from futuregreen.studio.models import Client, Collaborator, Employee

class Project(ProjectBase)
    """FutureGreen project. Extends projects.PhysicalProjectBase
    """

    designers = models.ManyToManyField(Employee)
    clients = models.ManyToManyField(Client)
    collaborators = models.ManyToManyField(Collaborator)

    tags = TaggableManager()
