# futuregreen/portfolio/models.py

from django.db import models

from taggit import TaggableManager

from projects.models import PhysicalProjectBase
from contacts.models import ContactBase

class Project(ProjectBase)
    """FutureGreen project. Extents projects.PhysicalProjectBase
    """

    tags = TaggableManager()

        
class Client(ContactBase):
    project = models.ForeignKey(Project)

class Collaborator(ContactBase):
    project = models.ForeignKey(Project)