# news/models.py

import os

from django.conf import settings
from django.db import models
from django.db.models import permalink

from taggit.managers import TaggableManager

from futuregreen.blocks.models import LinkBase, ArticleBase
from futuregreen.images.models import RelatedImageAutoBase

from futuregreen.portfolio.models import Project

class NewsItem(ArticleBase):
    """
        An article entry for a news item. Extends ArticleBase, and abstract model from django-backbeat-blocks.
    """

    class Meta:
        ordering = ('-date_published',)
        db_table = 'studio_newsitem'        

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
        Images for a news item.
    """
    news_item = models.ForeignKey(NewsItem)

    class Meta:
       	db_table = 'studio_newsitemimage'


class NewsItemFile(models.Model):
    """
        Files for a news item.
    """
    file = models.FileField(upload_to='files/news/', blank=True)
    news_item = models.ForeignKey(NewsItem)

    class Meta:
        db_table = 'studio_newsitemfile'

    def __unicode__(self):
        return u'%s' % os.path.basename(self.file.name)

class NewsItemProject(models.Model):
    """
        A project related to the article
    """
    project = models.ForeignKey(Project)
    article = models.ForeignKey(NewsItem)

    def __unicode__(self):
        return u'%s' % self.project.name

    class Meta:
        db_table = 'studio_newsitemproject'
