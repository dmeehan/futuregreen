# studio/models.py

from django.conf import settings
from django.db import models
from django.db.models import permalink

from taggit.managers import TaggableManager

from blocks.models import LinkBase, ArticleBase
from images.models import RelatedImageAutoBase

class NewsItem(ArticleBase):
    """
        An article entry for a news item
    """
    class Meta:
        ordering = ('-date_published',)

    @permalink
    def get_absolute_url(self):
        return ('newsitem_detail', None, {
            'year': self.date_published.year,
            'month': self.date_published.strftime('%b').lower(),
            'day': self.date_published.day,
            'slug': self.slug
        })

class NewsItemImage(RelatedImageAutoBase):
    """
        Images for a research entry.
    """
    item = models.ForeignKey(Item)

