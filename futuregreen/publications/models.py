# publications/models.py
import markdown

from django.db import models

from positions.fields import PositionField


class Publication(models.Model):
    """A model to display publications

    """
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=255, blank=True)
    coauthor = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    product_detail = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/publications", blank=True, null=True)
    

    purchase_link = models.URLField(max_length=255, blank=True)
    facebook_link = models.URLField(max_length=255, blank=True)
    twitter_link = models.URLField(max_length=255, blank=True)
    instagram_link = models.URLField(max_length=255, blank=True)

    slug = models.SlugField()
    

    # Fields to store generated HTML. 
    description_html = models.TextField(editable=False, blank=True)
    product_detail_html = models.TextField(editable=False, blank=True)

    order = PositionField()

    class Meta:
        ordering = ["order"]

    def render_markup(self):
        """Turns markup into HTML"""
        self.description_html = markdown.markdown(self.description)
        self.product_detail_html = markdown.markdown(self.product_detail)
    
    def save(self, force_insert=False, force_update=False):
        self.render_markup()
        super(Publication, self).save(force_insert, force_update)

    def __unicode__(self):
        return u'%s' % (self.title)

class PublicationLink(models.Model):
    """An external link related to a publication

    """

    publication = models.ForeignKey(Publication)

    title = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255)

    order = PositionField()

    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return u'%s' % (self.title)
