# studio/views.py
from django.shortcuts import render

from futuregreen.people.models import Employee
from futuregreen.news.models import Item

def index(request):
    news = Item._default_manager.latest('date_published')
    employee_list = Employee._default_manager.filter(status=employee.STATUS_FULL)
    return render(request, 'studio/studio_index.html', {'employee_list': employee_list,
                                          'news': news })