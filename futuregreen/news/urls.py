# news/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView, TemplateView

from futuregreen.news.models import Item

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Item, context_object_name = "news_list"), name = 'news_list'),
)