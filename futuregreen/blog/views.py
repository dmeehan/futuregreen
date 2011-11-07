# blog/views.py
from django.views.generic import ListView, DetailView

from futuregreen.blog.models import *

class EntryDetailView(DetailView):
    model = Item

class EntryListView(ListView):
    model = Item

