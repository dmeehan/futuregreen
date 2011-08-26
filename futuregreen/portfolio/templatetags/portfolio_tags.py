# portfolio/templatetags/porfolio_tags.py

from django import template
from futuregreen.portfolio.models import Project

def compose_featured(parser, token):
    return FeaturedNode()

class FeaturedNode(template.Node):
    def render(self, context):
        context['featured_project_list'] = Project.objects.live().featured()
        return ''
		
register = template.Library()
register.tag('get_featured_projects', compose_featured)