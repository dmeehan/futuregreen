# blog/templatetags/blog_tags.py

import re

from django import template
from django.conf import settings
from django.db import models

Entry = models.get_model('blog', 'entry')

register = template.Library()


class LatestEntries(template.Node):
    def __init__(self, limit, var_name):
        self.limit = int(limit)
        self.var_name = var_name

    def render(self, context):
        entries = Entry._default_manager.live()[:self.limit]
        if entries and (self.limit == 1):
            context[self.var_name] = entries[0]
        else:
            context[self.var_name] = entries
        return ''


@register.tag
def get_latest_entries(parser, token):
    """
Gets any number of latest posts and stores them in a varable.

Syntax::

{% get_latest_posts [limit] as [var_name] %}

Example usage::

{% get_latest_posts 10 as latest_post_list %}
"""
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    format_string, var_name = m.groups()
    return LatestEntries(format_string, var_name)