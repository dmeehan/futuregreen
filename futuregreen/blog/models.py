# blog/models.py  

from django.conf import settings
from django.db import models
from django.db.models import permalink

from taggit.managers import TaggableManager
import categories

from blocks.models import LinkBase, ArticleBase
from images.models import RelatedImageAutoBase

class Link(LinkBase):
    """
        A link entry for the blog
    """
    # taxonomy
    tags = TaggableManager(blank=True)
    categories = models.ManyToManyField('categories.Category')


class Entry(ArticleBase):
    """
        An article entry for the blog
    """
    enable_comments = models.BooleanField(default=True)
    links = models.ManyToManyField(Link)

    # taxonomy
    tags = TaggableManager(blank=True)
    categories = models.ManyToManyField('categories.Category')

    #auto-generated fields
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @permalink
    def get_absolute_url(self):
        return ('blog_entry_detail', [str(self.slug)])



class BlogEntryImage(RelatedImageAutoBase):
    """
        Images for a blog entry.
    """
    entry = models.ForeignKey(Entry)




class LinkImage(RelatedImageAutoBase):
    """
        Images for a link.
    """
    link = models.ForeignKey(Link)
