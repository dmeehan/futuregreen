# people/views.py

from django.views.generic import ListView, DetailView

from futuregreen.people.models import *

class EmployeeDetailView(DetailView):
    model = Employee

class EmployeeListView(ListView):
    model = Employee