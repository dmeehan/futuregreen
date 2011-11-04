# studio/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView, TemplateView

urlpatterns = patterns('',
    url(r'^$', 'futuregreen.studio.views.index', name = 'studio'),
    url(r'^news/$', TemplateView.as_view(template_name="studio/studio_news.html"), name='studio_news'),
    (r'^people/', include('futuregreen.people.urls')),
)