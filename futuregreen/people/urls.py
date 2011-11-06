# people/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView, TemplateView

from futuregreen.people.views import EmployeeDetailView, EmployeeListView

urlpatterns = patterns('',
    url(r'^$', EmployeeListView.as_view(), name = 'person_list'),
    url(r'^(?P<slug>[-\w]+)/$', EmployeeDetailView.as_view(), name = 'people_person_detail'),
)