# portfolio/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView, TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="studio/studio_index.html"), name='studio'),
    url(r'^$', TemplateView.as_view(template_name="studio/studio_news.html"), name='studio_news'),
)