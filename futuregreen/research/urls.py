# research/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView, TemplateView

from futuregreen.research.views import ArticleIndexView

urlpatterns = patterns('',
    url(r'^$', ArticleIndexView.as_view() , name = 'research'),
)