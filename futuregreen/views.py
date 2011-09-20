# futuregreen/views.py
from django.views.generic import ListView
from futuregreen.portfolio.models import Project

class IndexView(ListView):
    """
        Get the featured projects
    """
    context_object_name = "project_list"
    queryset = Project.objects.filter(featured=True)