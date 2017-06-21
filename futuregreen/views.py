# futuregreen/views.py

from django.shortcuts import render

from futuregreen.portfolio.models import Project
from futuregreen.news.models import NewsItem
from futuregreen.research.models import Article

def index(request):
    projects = Project._default_manager.live().filter(featured=True).order_by('?')
    project_list = list(projects)
    news = NewsItem._default_manager.live().latest('date_published')
    article = Article._default_manager.live().latest('date_published')
    return render(request, 'index.html', {'project_list': project_list,
                                          'news': news,
                                          'article': article })
