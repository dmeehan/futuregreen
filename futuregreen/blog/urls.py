# blog/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import DateDetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, WeekArchiveView, DayArchiveView, TodayArchiveView

from futuregreen.blog.models import *

urlpatterns = patterns('',
    url(r'^$', ArchiveIndexView.as_view(model=Entry), name = 'blog_entry_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        DateDetailView.as_view(model=Item, context_object_name = "item", date_field="date_published"),
        name = 'news_item_detail'),
)