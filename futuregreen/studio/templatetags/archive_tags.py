import re
from django import template
from futuregreen.research.models import Article

register = template.Library()

class ArticleArchive(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        dates = Article._default_manager.live().dates('date_published', 'month', order='DESC')
        if dates:
            context[self.var_name] = dates
        return ''

@register.tag
def get_article_archive(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    var_name = m.groups()[0]
    return ArticleArchive(var_name)