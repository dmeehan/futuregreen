# portfolio/templatetags/porfolio_tags.py

from django import template
from level0.portfolio.models import Discipline

def compose_disciplines(parser, token):
    return DisciplinesNode()

class DisciplinesNode(template.Node):
    def render(self, context):
        context['disciplines'] = Discipline.objects.all()
        return ''
		
register = template.Library()
register.tag('get_disciplines', compose_disciplines)