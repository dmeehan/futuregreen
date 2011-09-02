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

def resolve(var, context):
    try:
        return var.resolve(context)
    except VariableDoesNotExist:
        try:
            return var.var
        except AttributeError:
            return var
        
class TopLevelCategoriesNode(template.Node):
    def __init__(self, varname, model ):
        self.varname = varname
        self.model = model

    def render(self, context):
        context[self.varname] = ProjectTypes.objects.filter(parent=None).order_by('name')
        return ''

@register.tag
def do_get_top_level_categories(parser, token):
    """
Retrieves an alphabetical list of all the categories that have no parents.

Syntax::
{% get_top_level_categories as variablename %}

or optionally supply a different "category" model name:

{% get_top_level_categories appName.ModelName as variablename %}

Returns an list of categories [<category>, <category>, <category, ...]
"""
    m = get_model(app_label, model_name)
    
    bits = token.contents.split()
    if len(bits) != 4:
        raise template.TemplateSyntaxError(
            "Usage: {%% %s %s as <variable> %%}" % bits[0]
        )
    if bits[2] != 'as':
        raise template.TemplateSyntaxError(
            "Usage: {%% %s %s as <variable> %%}" % bits[0]
        )
    return TopLevelCategoriesNode(bits[2])