# publications/urls.py

from django.conf.urls import url, patterns

from .views import PublicationView

urlpatterns = patterns('',
    url(r'^$', PublicationView.as_view(), name='publications'),
)