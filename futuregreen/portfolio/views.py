# portfolio/views.py

from django.conf import settings
from django.db.models import get_model
from django.db.models import Max
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from categories.views import CategoryDetailView, CategoryRelatedList

from futuregreen.portfolio.models import Project, ProjectType, LandscapeType

class ProjectDetailView(DetailView):
    model = Project

class ProjectListView(ListView):
    queryset = Project._default_manager.filter(status=Project.STATUS_LIVE).order_by('-featured', '-date_end')
    paginate_by = settings.PROJECT_PAGINATE_BY

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['projecttype_list'] = ProjectType._default_manager.all()
        context['landscapetype_list'] = LandscapeType._default_manager.all()
        return context

class ProjectSizeAscListView(ProjectListView):
    queryset = Project._default_manager.size_asc()

class ProjectSizeListView(ProjectListView):
    queryset = Project._default_manager.live().order_by('area_normalized')

class ProjectSizeDescListView(ProjectListView):
    queryset = Project._default_manager.size_desc()

class ProjectDateListView(ProjectListView):
    pass

class ProjectCurrentListView(ProjectListView):
    pass

class ProjectCompletedListView(ProjectListView):
    pass

class TypeDetailView(CategoryDetailView):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TypeDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['projecttype_list'] = ProjectType._default_manager.all()
        context['landscapetype_list'] = LandscapeType._default_manager.all()
        return context

class ProjectTypeDetailView(TypeDetailView):
    model = ProjectType
    template_name = 'portfolio/projects_by_type.html'


class LandscapeTypeDetailView(TypeDetailView):
    model = LandscapeType
    template_name = 'portfolio/projects_by_landscape.html'
    