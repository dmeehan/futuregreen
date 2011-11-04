# news/views.py

from django.views.generic import ListView, DetailView

from futuregreen.news.models import *

class EmployeeDetailView(DetailView):
    model = Item

class EmployeeListView(ListView):
    model = Item