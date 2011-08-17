# projects/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.db.models import get_model

from futuregreen.projects.views import *

urlpatterns = patterns('',
   url(r'^$', ProjectListView.as_view(), name = 'projects_project_list'),
   url(r'^completed/$', ProjectCompletedListView.as_view(), name = 'projects_project_completed'),
   url(r'^current/$', ProjectCurrentListView.as_view(), name = 'projects_project_current'),
   url(r'^scale/asc/$', ProjectSizeAscListView.as_view(), name = 'projects_project_size_asc'),
   url(r'^scale/desc/$', ProjectSizeDescListView.as_view(), name = 'projects_project_size_desc'),
   url(r'^project/(?P<slug>[-\w]+)/$', ProjectDetailView.as_view(), name = 'projects_project_detail'),
)