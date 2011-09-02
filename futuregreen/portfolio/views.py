# portfolio/views.py

from django.conf import settings
from django.db.models import get_model
from django.db.models import Max
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from futuregreen.portfolio.models import Project, ProjectType, LandscapeType


class ProjectDetailView(DetailView):
    model = Project

class ProjectListView(ListView):
    queryset = Project._default_manager.live()
    paginate_by = settings.PROJECT_PAGINATE_BY

class ProjectSizeAscListView(ProjectListView):
    queryset = Project._default_manager.size_asc()

class ProjectSizeListView(ProjectListView):
    queryset = Project._default_manager.live()\
                .aggregate(max_area=Max('area_normalized'))

class ProjectSizeDescListView(ProjectListView):
    queryset = Project._default_manager.size_desc()

class ProjectDateListView(ProjectListView):
    pass

class ProjectCurrentListView(ProjectListView):
    pass

class ProjectCompletedListView(ProjectListView):
    pass

class ProjectProjectTypeListView(ProjectListView):
    def get_queryset(self):
        project_type = get_object_or_404(ProjectType, slug=self.args[0])
        return Project._default_manager.filter(project_types=project_type)

class ProjectLandscapeTypeListView(ProjectListView):
    def get_queryset(self):
        landscape_type = get_object_or_404(LandscapeType, slug=self.args[0])
        return Project._default_manager.filter(landscape_types=landscape_type)