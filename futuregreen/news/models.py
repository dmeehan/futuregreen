# blog/models.py

from django.conf import settings
from django.db import models
from django.db.models import permalink

from taggit_autosuggest.managers import TaggableManager

from blocks.models import LinkBase, ArticleBase
from images.models import RelatedImageAutoBase

class Item(ArticleBase):
    """
        An article entry for a news item
    """

    @permalink
    def get_absolute_url(self):
        return ('news_item_detail', None, {
            'year': self.date_published.year,
            'month': self.date_published.strftime('%b').lower(),
            'day': self.date_published.day,
            'slug': self.slug
        })

class ItemImage(RelatedImageAutoBase):
    """
        Images for a blog entry.
    """
    item = models.ForeignKey(Item)

