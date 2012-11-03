# studio/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from futuregreen.people.models import Employee
from futuregreen.portfolio.models import Project

def index(request):
    employee_list = Employee._default_manager.filter(public=True).order_by('employee_type__level')
    project_list = Project._default_manager.live().filter(featured=True).order_by('?')[:1]
    return render(request, 'studio/studio_index.html', {'employee_list': employee_list,
                                                        'project_list': project_list })


