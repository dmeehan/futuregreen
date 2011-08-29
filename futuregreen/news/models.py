# blog/models.py

from django.conf import settings
from django.db import models
from django.db.models import permalink

from taggit.managers import TaggableManager
import categories

from blocks.models import LinkBase, ArticleBase
from images.models import RelatedImageAutoBase

class Item(ArticleBase):
    """
        An article entry for a news item
    """

    @permalink
    def get_absolute_url(self):
        return ('news_item_detail', None, {
            'year': self.publish.year,
            'month': self.publish.strftime('%b').lower(),
            'day': self.publish.day,
            'slug': self.slug
        })

class ItemImage(RelatedImageAutoBase):
    """
        Images for a blog entry.
    """
    item = models.ForeignKey(Item)

