# projects/views.py

from django.conf import settings
from django.db.models import get_model
from django.views.generic import ListView, DetailView

from projects.models import Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectListView(ListView):
    queryset = Project._default_manager.live()
    context_object_name="project_list",
    paginate_by = settings.PROJECT_PAGINATE_BY
    template = '/projects/project_list.html'

class ProjectSizeAscListView(ProjectListView):
    queryset = Project._default_manager.live().size_asc()

class ProjectSizeDescListView(ProjectListView):
    queryset = Project._default_manager.live().size_desc()

class ProjectDateListView(ProjectListView):
    queryset = Project._default_manager.live()

class ProjectCurrentListView(ProjectListView):
    queryset = Project._default_manager.live().current()

class ProjectCompletedListView(ProjectListView):
    queryset = Project._default_manager.live().completed()