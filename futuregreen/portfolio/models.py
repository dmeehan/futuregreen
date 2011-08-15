# futuregreen/portfolio/models.py

from django.contrib.contenttypes import generic
from django.db import models

from imagekit.models import ImageModel
from taggit.managers import TaggableManager

from projects.models import PhysicalProjectBase
from media.models import GenericRelatedImageBase

from futuregreen.studio.models import Client, Collaborator, Employee

class Project(PhysicalProjectBase):
    """
        FutureGreen project. Extends projects.PhysicalProjectBase
        
    """

    # relations
    designers = models.ManyToManyField(Employee, blank=True, null=True)
    clients = models.ManyToManyField(Client, blank=True, null=True)
    collaborators = models.ManyToManyField(Collaborator, blank=True, null=True)

    # taxonomy
    tags = TaggableManager(blank=True)


class ProjectImage(ImageModel, GenericRelatedImageBase):
    """
        Images for a project.

    """

    CROPHORZ_LEFT = 0
    CROPHORZ_CENTER = 1
    CROPHORZ_RIGHT = 2
    CROPHORZ_CHOICES = (
        (CROPHORZ_LEFT, 'left'),
        (CROPHORZ_CENTER, 'center'),
        (CROPHORZ_RIGHT, 'RIGHT'),
    )

    CROPVERT_TOP = 0
    CROPVERT_CENTER = 1
    CROPVERT_BOTTOM = 2
    CROPVERT_CHOICES = (
        (CROPVERT_TOP, 'TOP'),
        (CROPVERT_CENTER, 'CENTER'),
        (CROPVERT_BOTTOM, 'BOTTOM'),
    )

    project = generic.GenericRelation(Project)

    crop_horz = models.PositiveSmallIntegerField(
                    verbose_name='horizontal cropping',
                    choices=CROPHORZ_CHOICES,
                    blank=True,
                    default=CROPHORZ_CENTER,
                    help_text="From where to horizontally crop the image, if cropping is necessary.")

    crop_vert = models.PositiveSmallIntegerField(
                    verbose_name='vertical cropping',
                    choices=CROPVERT_CHOICES,
                    blank=True,
                    default=CROPVERT_CENTER,
                    help_text="From were to vertically crop the image, if cropping is necessary.")

    class IKOptions:
        spec_module = 'futuregreen.portfolio.imagespecs'
        cache_dir = 'images/resized'