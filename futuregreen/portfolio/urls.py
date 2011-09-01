# portfolio/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView

from categories.views import CategoryDetailView, CategoryRelatedList

from futuregreen.portfolio.views import *
from futuregreen.portfolio.models import ProjectType

urlpatterns = patterns('',
    url(r'^projects/$', ProjectListView.as_view(), name='portfolio_project_list'),
    url(r'^projects/completed/$', ProjectCompletedListView.as_view(), name='portfolio_project_completed'),
    url(r'^projects/current/$', ProjectCurrentListView.as_view(), name = 'portfolio_project_current'),
    url(r'^projects/scale/ascending/$', ProjectSizeAscListView.as_view(), name = 'portfolio_project_area_asc'),
    url(r'^projects/scale/descending/$', ProjectSizeDescListView.as_view(), name = 'portfolio_project_area_desc'),
    url(r'^project/(?P<slug>[-\w]+)/$', ProjectDetailView.as_view(), name = 'portfolio_project_detail'),

    url(r'^projects/projecttypes/$', ListView.as_view(queryset = ProjectType._default_manager.filter(level=0)),
        name = 'categories_tree_list'),
    url(r'^projects/projecttypes/(?P<path>.+)/$', CategoryDetailView.as_view(model=ProjectType,
        template_name = 'portfolio/projects_by_type.html'), name = 'portfolio_projects_by_type'),
)