# publications/urls.py

from django.conf.urls.defaults import patterns, url

from .views import PublicationView

urlpatterns = patterns('',
    url(r'^$', PublicationView.as_view(), name='publications'),
)