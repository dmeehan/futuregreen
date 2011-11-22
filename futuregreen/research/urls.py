# research/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView, TemplateView

urlpatterns = patterns('',
    url(r'^$', 'futuregreen.research.views.index', name = 'research'),
    (r'^research/', include('futuregreen.research.urls')),
    (r'^news/', include('futuregreen.news.urls')),
)