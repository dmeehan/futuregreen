# projects/views.py

from django.conf import settings
from django.db.models import get_model
from django.views.generic import ListView, DetailView

from futuregreen.projects.models import Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectListView(ListView):
    model = Project
    context_object_name="project_list",
    paginate_by = settings.PROJECT_PAGINATE_BY
    template = '/projects/project_list.html'

class ProjectSizeAscListView(ProjectListView):
    pass

class ProjectSizeDescListView(ProjectListView):
    pass

class ProjectDateListView(ProjectListView):
    pass

class ProjectCurrentListView(ProjectListView):
    pass

class ProjectCompletedListView(ProjectListView):
    pass