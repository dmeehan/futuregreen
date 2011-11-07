# blog/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import DateDetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, WeekArchiveView, DayArchiveView, TodayArchiveView

from futuregreen.blog.models import *
from futuregreen.blog.views import *

urlpatterns = patterns('',
    url(r'^$', EntryIndexView.as_view(), name = 'blog_entry_index'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        EntryDetailView.as_view(),
        name = 'blog_entry_detail'),
)