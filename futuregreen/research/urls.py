# research/urls.py

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import YearArchiveView, MonthArchiveView,\
    WeekArchiveView, DayArchiveView, TodayArchiveView, \
    DetailView, ListView, TemplateView

from taggit.views import tagged_object_list

from futuregreen.research.models import Article
from futuregreen.research.views import ArticleIndexView, ArticleDetailView

urlpatterns = patterns('',
    url(r'^$', ArticleIndexView.as_view() , name = 'research'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        ArticleDetailView.as_view(), name = 'research_article_detail'),
     url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',
        DayArchiveView.as_view(
        queryset=Article._default_manager.live(),
        date_field="date_published"),
        name='article_archive_day'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
        MonthArchiveView.as_view(
        queryset=Article._default_manager.live(),
        date_field="date_published"),
        name='article_archive_month'
    ),
    url(r'^(?P<year>\d{4})/$',
        YearArchiveView.as_view(
        queryset=Article._default_manager.live(),
        date_field="date_published"),
        name='article_archive_year'
    ),
    url(r'^tag/(?P<slug>[-\w]+)/$',
        tagged_object_list(queryset=Article._default_manager.live,
                           template_name='articles_by_tag.html',
                           template_object_name='article'),
        name='articles_by_tag'
    ),
)