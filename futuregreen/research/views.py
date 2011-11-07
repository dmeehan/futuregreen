# research/views.py

from django.shortcuts import render

from futuregreen.blog.models import Entry
from futuregreen.portfolio.models import Project

def index(request):
    entry = Entry._default_manager.latest('date_published')
    project_list = Project._default_manager.live().filter(featured=True).order_by('?')[:1]
    return render(request, 'studio/studio_index.html', {'project_list': project_list,
                                                        'entry': entry })
