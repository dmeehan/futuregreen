# blog/models.py  

from django.conf import settings
from django.db import models
from django.db.models import permalink

from taggit.managers import TaggableManager
from categories.models import Category

from blocks.models import LinkBase, ArticleBase
from images.models import RelatedImageAutoBase

class Link(LinkBase):
    """
        A link entry for the blog
    """
    # taxonomy
    tags = TaggableManager(blank=True)


class Entry(ArticleBase):
    """
        An article entry for the blog
    """
    enable_comments = models.BooleanField(default=True)
    links = models.ManyToManyField(Link)

    # taxonomy
    tags = TaggableManager(blank=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)

    @permalink
    def get_absolute_url(self):
        return ('blog_entry_detail', None, {
            'year': self.date_published.year,
            'month': self.date_published.strftime('%b').lower(),
            'day': self.date_published.day,
            'slug': self.slug
        })

    
class EntryImage(RelatedImageAutoBase):
    """
        Images for a blog entry.
    """
    entry = models.ForeignKey(Entry)



class LinkImage(RelatedImageAutoBase):
    """
        Images for a link.
    """
    link = models.ForeignKey(Link)
