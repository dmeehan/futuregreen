# portfolio/views.py

from django.conf import settings
from django.db.models import get_model
from django.views.generic import ListView, DetailView

from futuregreen.portfolio.models import Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectListView(ListView):
    queryset = Project._default_manager.live()
    paginate_by = settings.PROJECT_PAGINATE_BY

class ProjectSizeAscListView(ProjectListView):
    queryset = Project._default_manager.size_asc()

class ProjectSizeDescListView(ProjectListView):
    queryset = Project._default_manager.size_desc()

class ProjectDateListView(ProjectListView):
    pass

class ProjectCurrentListView(ProjectListView):
    pass

class ProjectCompletedListView(ProjectListView):
    pass