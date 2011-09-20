# portfolio/templatetags/porfolio_tags.py

from django import template
from django.template import Library, Node, TemplateSyntaxError, \
    Variable, resolve_variable, VariableDoesNotExist, Context

from categories.models import Category
from mptt.utils import drilldown_tree_for_node
from mptt.templatetags.mptt_tags import tree_path, tree_info
from futuregreen.portfolio.models import Project, ProjectType, LandscapeType

register = template.Library()

register.filter("category_path", tree_path)
register.filter(tree_info)

def compose_featured(parser, token):
    return FeaturedNode()

class FeaturedNode(template.Node):
    def render(self, context):
        context['featured_project_list'] = Project.objects.live().filter(featured=True)
        return ''
	
register.tag('get_featured_projects', compose_featured)