# futuregreen/portfolio/urls.py

from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView

from futuregreen.portfolio.models import *

urlpatterns = patterns('',

    # portfolio index
    url(r'^projects/$',
        ListView.as_view(model=Project, context_object_name = "project_list"),
        name="projects_project_list"),

    url(r'^projects/project/(?P<slug>[-\w]+)/$',
        DetailView.as_view(model=Project, context_object_name = "project"),
        name="projects_project_detail"),

)