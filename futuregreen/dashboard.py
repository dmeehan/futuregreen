"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'futuregreen.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for futuregreenstudio
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append a Group module for "Site Content"
        self.children.append(modules.Group(
            title="Site Content",
            column=1,
            collapsible=True,
            children=[
                 modules.ModelList(
                    css_classes=('collapse open',),
                    title='Portfolio',
                    models=('futuregreen.portfolio.*',)
                ),
                modules.ModelList(
                    css_classes=('collapse open',),
                    title='People',
                    models=('futuregreen.people.*',)
                ),
                modules.ModelList(
                    css_classes=('collapse open',),
                    title='News',
                    models=('futuregreen.news.*',)
                ),
                modules.ModelList(
                    css_classes=('collapse open',),
                    title='Research',
                    models=('futuregreen.research.*',)
                ),
                modules.ModelList(
                    css_classes=('collapse open',),
                    title='Content Blocks',
                    models=('futuregreen.content.*',)
                ),
            ]
        ))
        
        # append a model list module for "Site Organization"
        self.children.append(modules.ModelList(
            _('Site Organization'),
            collapsible=True,
            column=1,
            css_classes=('collapse open',),
            models=('categories.*','taggit.*', 'django_generic_flatblocks.*'),
        ))
        
        # append a model list module for "Administration"
        self.children.append(modules.ModelList(
            _('Site Administration'),
            column=1,
            css_classes=('collapse closed',),
            models=('django.contrib.*',),
        ))

        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


