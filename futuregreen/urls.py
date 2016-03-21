from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView, ListView, DetailView, RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # redirects
    (r'^website/', RedirectView.as_view(url='/')),
    (r'^newsfeed/', RedirectView.as_view(url='/news/')),
    (r'^studio/news/', RedirectView.as_view(url='/news/')),

    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    
    url(r'^$', 'futuregreen.views.index', name = 'home'),
    #url(r'^$', TemplateView.as_view(template_name='site_down.html'), name = 'home'),

    # portfolio
    (r'^portfolio/', include('futuregreen.portfolio.urls')),

    # studio
    (r'^studio/', include('futuregreen.studio.urls')),

    # news
    (r'^news/', include('futuregreen.news.urls')),

    # research
    (r'^research/', include('futuregreen.research.urls')),

    # book
    #(r'^book/', include('futuregreen.publications.urls')),

    # contact
    url(r'^contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    
)
