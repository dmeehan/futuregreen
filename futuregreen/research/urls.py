# research/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView, TemplateView

from futuregreen.research.views import ArticleIndexView, ArticleDetailView

urlpatterns = patterns('',
    url(r'^$', ArticleIndexView.as_view() , name = 'research'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        ArticleDetailView.as_view(), name = 'research_article_detail'),
)