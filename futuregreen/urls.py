from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    
    (r'^$', TemplateView.as_view(template_name="index.html")),

    # portfolio
    (r'^portfolio/', include('futuregreen.portfolio.urls')),
    
)