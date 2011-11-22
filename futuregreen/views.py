# futuregreen/views.py
from django.shortcuts import render

from futuregreen.portfolio.models import Project
from futuregreen.news.models import Item

def index(request):
    projects = Project._default_manager.live().filter(featured=True).order_by('?')
    project_list = list(projects)
    news = Newsitem._default_manager.latest('date_published')
    return render(request, 'index.html', {'project_list': project_list,
                                          'news': news })