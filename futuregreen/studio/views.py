# studio/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from futuregreen.studio.models import NewsItem
from futuregreen.people.models import Employee
from futuregreen.portfolio.models import Project

def index(request):
    news = NewsItem._default_manager.latest('date_published')
    principal_list = Employee._default_manager.filter(public=True, employee_type__name='Principal')
    associate_list = Employee._default_manager.filter(public=True, employee_type__name='Associate')
    staff_list = Employee._default_manager.filter(public=True, employee_type__name='Staff')
    employee_list = Employee._default_manager.filter(public=True).order_by('employee_type__level')
    project_list = Project._default_manager.live().filter(featured=True).order_by('?')[:1]
    return render(request, 'studio/studio_index.html', {'employee_list': employee_list,
                                                        'project_list': project_list,
                                                        'news': news })


class NewsDetailView(DetailView):
    model = NewsItem

class NewsListView(ListView):
    model = NewsItem

