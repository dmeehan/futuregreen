# projects/models.py

from decimal import Decimal

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.utils.html import strip_tags

from imagekit.models import ImageModel
from taggit.managers import TaggableManager
import categories
from easy_maps.models import Address

from futuregreen.contacts.models import Client, Collaborator, Employee
from futuregreen.media.models import ImageBase
from futuregreen.projects.managers import ProjectManager
from futuregreen.projects.fields import PositionField

class ProjectBase(models.Model):
    """
    
        An abstract base class for a project.
    
    """
    
    # project status choices 
    STATUS_LIVE = 1
    STATUS_HIDDEN = 2
    STATUS_PENDING = 3
    STATUS_DRAFT = 4
    STATUS_CHOICES = (
        (STATUS_LIVE, 'Live'),
        (STATUS_PENDING, 'Pending'),
        (STATUS_DRAFT, 'Draft'),
        (STATUS_HIDDEN, 'Hidden'),
    )
    
    # Core fields
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=250)
    short_description = models.TextField()
    description = models.TextField()
    date_start = models.DateField("start date",
                                  blank=True, null=True,
                                  help_text="Leave blank if project is in promo.")
    date_end = models.DateField("end date",
                                blank=True, null=True,
                                help_text="Leave blank if project is in progress.")

    external_url = models.URLField(blank=True,help_text="Optional.")
    
    # Metadata.
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
                                              default=STATUS_LIVE,
                                              help_text="Only projects with live status will be publicly displayed.")
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from title. Must be unique.")

    #autogenerated fields
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)

    # Fields to store generated HTML.
    description_html = models.TextField(editable=False, blank=True)
    
    class Meta:
        abstract = True
        ordering = ('-date_end','name',)

    @permalink
    def get_absolute_url(self):
        return ('projects_project_detail', [str(self.slug)])
        
    def __unicode__(self):
        return u'%s' % self.name
    
    def render_markup(self):
        """Turns any markup into HTML"""
        original = self.description_html

        if PROJECT_MARKUP == 'markdown':
            import markdown
            self.description_html = markdown.markdown(self.description)
        elif PROJECT_MARKUP == 'textile':
            import textile
            self.description_html = textile.textile(self.description)
        elif PROJECT_MARKUP == 'wysiwyg':
            self.description_html = self.description
        elif PROJECT_MARKUP == 'html':
            self.description_html = self.description
        else:
            self.description_html = strip_tags(self.description)

        return self.description_html != original

    def save(self, force_insert=False, force_update=False):
        self.render_markup()
        super(ProjectBase, self).save(force_insert, force_update)
        
    
class PhysicalMixin(models.Model):
    """

        Fields and methods for a
        physically constructable design project.

    """
    # project size unit choices
    UNIT_SQUAREFOOT = 1
    UNIT_SQUAREMETER = 2
    UNIT_ACRE = 3
    UNIT_HECTARE = 4
    UNIT_CHOICES = (
        (UNIT_SQUAREFOOT, 'square feet'),
        (UNIT_SQUAREMETER, 'square meters'),
        (UNIT_ACRE, 'acres'),
        (UNIT_HECTARE, 'hectares'),
    )
    
    UNIT_CONVERSIONS = {
        (UNIT_SQUAREFOOT, UNIT_SQUAREMETER): Decimal(.0929),
        (UNIT_SQUAREFOOT, UNIT_ACRE): Decimal(.000023),
        (UNIT_SQUAREFOOT, UNIT_HECTARE): Decimal(.0000093),
        (UNIT_SQUAREMETER, UNIT_SQUAREFOOT): Decimal(10.76),
        (UNIT_SQUAREMETER, UNIT_ACRE): Decimal(.00025),
        (UNIT_SQUAREMETER, UNIT_HECTARE): Decimal(.0001),
        (UNIT_ACRE, UNIT_SQUAREFOOT): Decimal(43560),
        (UNIT_ACRE, UNIT_SQUAREMETER): Decimal(4047),
        (UNIT_ACRE, UNIT_HECTARE): Decimal(.4047),
        (UNIT_HECTARE, UNIT_SQUAREFOOT): Decimal(107639.10),
        (UNIT_HECTARE, UNIT_SQUAREMETER): Decimal(10000.00),
        (UNIT_HECTARE, UNIT_ACRE): Decimal(2.47),
    }


    area = models.DecimalField(max_digits=12, decimal_places=2)
    unit = models.PositiveSmallIntegerField(choices=UNIT_CHOICES,
                                     default=UNIT_SQUAREFOOT,
                                     help_text="Unit of measurement.")

    area_normalized = models.DecimalField(max_digits=12, decimal_places=2, editable=False)

    class Meta:
        abstract = True

    def convert(self, someUnit):
        if someUnit == self.unit:
            return self.area
        elif (self.unit, someUnit) in self.UNIT_CONVERSIONS:
            return self.area * self.UNIT_CONVERSIONS[(self.unit, someUnit)]
        else:
            raise Exception("Can't convert")

    @property
    def square_feet(self):
        return self.convert(self.UNIT_SQUAREFOOT)

    @property
    def square_meters(self):
        return self.convert(self.UNIT_SQUAREMETER)

    @property
    def acres(self):
        return self.convert(self.UNIT_ACRE)

    @property
    def hectares(self):
        return self.convert(self.UNIT_HECTARE)

    def save(self, force_insert=False, force_update=False):
        self.area_normalized = self.convert(self.UNIT_SQUAREFOOT)
        super(PhysicalMixin, self).save(force_insert, force_update)

class Project(ProjectBase, PhysicalMixin):
    """
        FutureGreen project. Extends projects.PhysicalProjectBase

    """
    objects = ProjectManager()

    #address
    address = models.ForeignKey(Address, blank=True, null=True)
    
    # relations
    designers = models.ManyToManyField(Employee, blank=True, null=True)
    clients = models.ManyToManyField(Client, blank=True, null=True)
    collaborators = models.ManyToManyField(Collaborator, blank=True, null=True)

    # taxonomy
    tags = TaggableManager(blank=True)
    categories = models.ManyToManyField('categories.Category')


class ProjectImage(ImageModel, ImageBase):
    """
        Images for a project.

    """
    project = models.ForeignKey(Project)
    order = PositionField(unique_for_field='project')
    is_main = models.BooleanField('Main image', default=False)

    CROPHORZ_LEFT = 0
    CROPHORZ_CENTER = 1
    CROPHORZ_RIGHT = 2
    CROPHORZ_CHOICES = (
        (CROPHORZ_LEFT, 'left'),
        (CROPHORZ_CENTER, 'center'),
        (CROPHORZ_RIGHT, 'right'),
    )

    CROPVERT_TOP = 0
    CROPVERT_CENTER = 1
    CROPVERT_BOTTOM = 2
    CROPVERT_CHOICES = (
        (CROPVERT_TOP, 'top'),
        (CROPVERT_CENTER, 'center'),
        (CROPVERT_BOTTOM, 'bottom'),
    )

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

    class Meta:
        ordering = ['order',]
    
    def get_upload_path(self, filename):
        related_project = str(self.project.slug)

        root, ext = os.path.splitext(filename)
        return os.path.join('images', 'projects', related_project,
                            self.filename + ext)

    def save(self, *args, **kwargs):
        if self.is_main:
            related_images = self._default_manager.filter(
                project=self.project)
            related_images.update(is_main=False)

        super(ProjectImage, self).save(*args, **kwargs)

    class IKOptions:
        spec_module = 'futuregreen.projects.imagespecs'
        cache_dir = 'images/projects/resized'

