# projects/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.db.models import get_model

from futuregreen.projects.views import *

urlpatterns = patterns('',
   url(r'^projects/$', ProjectListView.as_view(), name = 'projects_project_list'),
   url(r'^projects/completed/$', ProjectCompletedListView.as_view(), name = 'projects_project_completed'),
   url(r'^projects/current/$', ProjectCurrentListView.as_view(), name = 'projects_project_current'),
   url(r'^projects/scale/asc/$', ProjectSizeAscListView.as_view(), name = 'projects_project_size_asc'),
   url(r'^projects/scale/desc/$', ProjectSizeDescListView.as_view(), name = 'projects_project_size_desc'),
   url(r'^projects/project/(?P<slug>[-\w]+)/$', ProjectDetailView.as_view(), name = 'projects_project_detail'),
)