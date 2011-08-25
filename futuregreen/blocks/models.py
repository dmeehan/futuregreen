# blocks/models.py

import datetime

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.db.models import permalink
from django.utils.html import strip_tags


class TextBlockBase(models.Model):
    """
        An abstract content block with
        optional title, excerpt, and body fields.
    """
    title = models.CharField(max_length=255, blank=True)
    excerpt = models.TextField(blank=True)
    body = models.TextField(blank=True)

    # Fields to store generated HTML. For use with a markup syntax such as Markdown or Textile
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    def render_markup(self):
        """Turns any markup into HTML"""
        if settings.BLOCKS_MARKUP == 'markdown':
            import markdown
            self.body_html = markdown.markdown(self.body)
            self.excerpt_html = markdown.markdown(self.excerpt)
        elif settings.BLOCKS_MARKUP == 'textile':
            import textile
            self.body_html = textile.textile(self.body)
            self.excerpt_html = textile.markdown(self.excerpt)
        elif settings.BLOCKS_MARKUP == 'wysiwyg':
            self.body_html = self.body
            self.excerpt_html = self.excerpt
        elif settings.BLOCKS_MARKUP == 'html':
            self.body_html = self.body
            self.excerpt_html = self.excerpt
        else:
            self.body_html = strip_tags(self.body)
            self.excerpt_html = strip_tags(self.excerpt)

    def is_empty(self):
        if not self.title and not self.body and not self.excerpt:
            return True

    def clean(self):
        if self.is_empty():
            raise ValidationError('You must include content in either of title, body, or excerpt.')

    def save(self, force_insert=False, force_update=False):
        self.render_markup()
        super(TextBlockBase, self).save(force_insert, force_update)

    def __unicode__(self):
        if self.title:
            return self.title
        elif self.excerpt:
            return self.excerpt[:20]
        elif self.body:
            return self.body[:20]
        else:
            return "Textblock: %s" % self.pk

    class Meta:
        abstract = True


class StatusMixin(models.Model):
    """
        Allow for a content block to be marked with a status

    """

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

    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
                                              default=STATUS_LIVE,
                                              help_text="Only content with live status will be publicly displayed.")

    class Meta:
        abstract = True

        
class PostMixin(models.Model):
    """
        A mixin for a posted content type.
    """

    # metadata
    posted_by = models.ForeignKey(User)
    date_published = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='date_published')

    class Meta:
        abstract = True
        ordering = ['-date_published']


class PostBase(PostMixin, StatusMixin):
    class Meta:
        abstract = True

class LinkBase(PostBase):
    """
        A link to another website.
    """

    url = models.URLField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True

    @permalink
    def get_absolute_url(self):
        return ('blocks_link_detail', [str(self.slug)])


class ArticleBase(PostBase, TextBlockBase):
    """
        A blog type article
    """
    class Meta:
        abstract = True

    @permalink
    def get_absolute_url(self):
        return ('blocks_article_detail', [str(self.slug)])
    



