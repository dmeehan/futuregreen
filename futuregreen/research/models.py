# research/models.py

from django.conf import settings
from django.db import models
from django.db.models import permalink

from taggit.managers import TaggableManager
from categories.models import Category

from futuregreen.blocks.models import LinkBase, ArticleBase
from futuregreen.images.models import RelatedImageAutoBase

from futuregreen.portfolio.models import Project


class Article(ArticleBase):
    """
        A research article authored by Future Green Studio
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
        Images for a research article.
    """
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return '%s image %d' % (self.article.title, self.order)

class ArticleFile(models.Model):
    """
        Files for a news item.
    """
    file = models.FileField(upload_to='files/article/', blank=True)
    news_item = models.ForeignKey(Article)

class ArticleProject(models.Model):
    """
        A project related to the article
    """
    project = models.ForeignKey(Project)
    article = models.ForeignKey(Article)

