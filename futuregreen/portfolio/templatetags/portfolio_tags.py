# portfolio/templatetags/porfolio_tags.py

import re

from django import template
from django.conf import settings
from django.db import models


from futuregreen.portfolio.models import Project

register = template.Library()

def compose_featured(parser, token):
    return FeaturedNode()

class FeaturedNode(template.Node):
    def render(self, context):
        context['featured_project_list'] = Project._default_manager.live().filter(featured=True)
        return ''
	
register.tag('get_featured_projects', compose_featured)


class LatestProjects(template.Node):
    def __init__(self, limit, var_name):
        self.limit = int(limit)
        self.var_name = var_name

    def render(self, context):
        news = Project._default_manager.live()[:self.limit]
        if news and (self.limit == 1):
            context[self.var_name] = news[0]
        else:
            context[self.var_name] = news
        return ''


@register.tag
def get_latest_projects(parser, token):
    """
Gets any number of latest projects and stores them in a variable.

Syntax::

{% get_latest_projects [limit] as [var_name] %}

Example usage::

{% get_latest_projects 10 as latest_project_list %}
"""
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    format_string, var_name = m.groups()
    return LatestProjects(format_string, var_name)


class ProjectArchive(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        dates = Project._default_manager.live().dates('date_published', 'month', order='DESC')
        if dates:
            context[self.var_name] = dates
        return ''

@register.tag
def get_project_archive(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    var_name = m.groups()[0]
    return ProjectArchive(var_name)



