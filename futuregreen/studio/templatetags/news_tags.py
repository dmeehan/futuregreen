# studio/templatetags/news_tags.py

import re

from django import template
from django.conf import settings
from django.db import models


from futuregreen.studio.models import NewsItem

register = template.Library()


class LatestNews(template.Node):
    def __init__(self, limit, var_name):
        self.limit = int(limit)
        self.var_name = var_name

    def render(self, context):
        news = NewsItem._default_manager.live()[:self.limit]
        if news and (self.limit == 1):
            context[self.var_name] = news[0]
        else:
            context[self.var_name] = news
        return ''


@register.tag
def get_latest_news(parser, token):
    """
Gets any number of latest news items and stores them in a variable.

Syntax::

{% get_latest_news [limit] as [var_name] %}

Example usage::

{% get_latest_news 10 as latest_news_list %}
"""
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    format_string, var_name = m.groups()
    return LatestNews(format_string, var_name)


class NewsArchive(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        dates = NewsItem._default_manager.live().dates('date_published', 'month', order='DESC')
        if dates:
            context[self.var_name] = dates
        return ''

@register.tag
def get_news_archive(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    var_name = m.groups()[0]
    return NewsArchive(var_name)