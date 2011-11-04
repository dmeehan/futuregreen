# studio/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView, TemplateView

urlpatterns = patterns('',
    url(r'^$', 'futuregreen.studio.views.index', name = 'studio'),
    (r'^people/', include('futuregreen.people.urls')),
    (r'^news/', include('futuregreen.news.urls')),
)