# studio/views.py
from django.shortcuts import render

from futuregreen.people.models import Employee
from futuregreen.news.models import Item
from futuregreen.portfolio.models import Project

def index(request):
    news = Item._default_manager.latest('date_published')
    employee_list = Employee._default_manager.filter(status=Employee.STATUS_FULL)
    project_list = Project._default_manager.live().filter(featured=True).order_by('?')[:4]
    return render(request, 'studio/studio_index.html', {'employee_list': employee_list,
                                                        'project_list': project_list,
                                                        'news': news })