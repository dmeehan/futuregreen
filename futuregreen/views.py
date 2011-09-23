# futuregreen/views.py
from django.shortcuts import render

from futuregreen.portfolio.models import Project
from futuregreen.news.models import Item
def index(request):
    projects = Project._default_manager.live().filter(featured=True).order_by('?')
    project_list = list(projects)
    item = Item._default_manager.live().latest()
    return render(request, 'index.html', {'project_list': project_list,
                                          'item': item })