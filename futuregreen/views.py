# futuregreen/views.py
from django.shortcuts import render

from futuregreen.portfolio.models import Project

def index(request):
    projects = Project._default_manager.live().filter(featured=True).order_by('?')
    project_list = list(projects)
    return render(request, 'index.html', {'project_list': project_list})