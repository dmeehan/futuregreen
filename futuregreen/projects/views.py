# projects/views.py

from django.db.models import get_model
from django.views.generic import ListView, DetailView


class ProjectDetailView(DetailView):
    pass
        

class ProjectListView(ListView):
    #queryset = project_model._default_manager.live()
    context_object_name="project_list",
    #paginate_by = PROJECT_PAGINATE_BY
    template = '/projects/project_list.html'

class ProjectSizeAscListView(ProjectListView):
    pass
    #queryset = project_model._default_manager.live().size_asc()

class ProjectSizeDescListView(ProjectListView):
    pass
    #queryset = project_model._default_manager.live().size_desc()

class ProjectDateListView(ProjectListView):
    pass
    #queryset = project_model._default_manager.live()

class ProjectCurrentListView(ProjectListView):
    pass
    #queryset = project_model._default_manager.live().current()

class ProjectCompletedListView(ProjectListView):
    pass
    #queryset = project_model._default_manager.live().completed()