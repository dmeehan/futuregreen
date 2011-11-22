# studio/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView, TemplateView, DateDetailView
from futuregreen.news.models import Item

urlpatterns = patterns('',
    url(r'^$', 'futuregreen.studio.views.index', name = 'studio'),
    (r'^people/', include('futuregreen.people.urls')),
    url(r'^news/', ListView.as_view(model=Item, context_object_name = "news_list"), name = 'newsitem_list'),
    url(r'^news/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        DateDetailView.as_view(model=Item, context_object_name = "item", date_field="date_published"),
        name = 'newsitem_detail'),
)