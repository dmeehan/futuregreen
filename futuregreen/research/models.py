# research/models.py

from django.conf import settings
from django.db import models
from django.db.models import permalink

from taggit.managers import TaggableManager
from categories.models import Category

from blocks.models import LinkBase, ArticleBase
from images.models import RelatedImageAutoBase


class Article(ArticleBase):
    """
        An article entry for the research
    """
    enable_comments = models.BooleanField(default=True)
    url = models.URLField(blank=True)

    # taxonomy
    tags = TaggableManager(blank=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)

    @permalink
    def get_absolute_url(self):
        return ('research_article_detail', None, {
            'year': self.date_published.year,
            'month': self.date_published.strftime('%b').lower(),
            'day': self.date_published.day,
            'slug': self.slug
        })

    
class ArticleImage(RelatedImageAutoBase):
    """
        Images for a research entry.
    """
    entry = models.ForeignKey(Entry)

