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
    url(r'^projects/scale/$', ProjectSizeListView.as_view(), name = 'portfolio_project_area'),
    url(r'^projects/scale/ascending/$', ProjectSizeAscListView.as_view(), name = 'portfolio_project_area_asc'),
    url(r'^projects/scale/descending/$', ProjectSizeDescListView.as_view(), name = 'portfolio_project_area_desc'),
    url(r'^project/(?P<slug>[-\w]+)/$', ProjectDetailView.as_view(), name = 'portfolio_project_detail'),

    url(r'^projects/projecttypes/(?P<path>.+)/$',
        ProjectTypeDetailView.as_view(), name = 'portfolio_projects_by_type'),
    url(r'^projects/landscapetypes/(?P<path>.+)/$',
        LandscapeTypeDetailView.as_view(), name = 'portfolio_projects_by_landscape'),
)