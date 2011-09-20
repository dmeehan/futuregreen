from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib import admin
admin.autodiscover()

from futuregreen.portfolio.models import Project

urlpatterns = patterns('',
    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    
    url(r'^$', ListView.as_view(context_object_name = "project_list",
        queryset = Project._default_manager.live().filter(featured=True).order_by("?")[:10:1],
        template_name = "index.html",),
        name = 'home'),

    # portfolio
    (r'^portfolio/', include('futuregreen.portfolio.urls')),
    
)