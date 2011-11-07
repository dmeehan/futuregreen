# news/views.py

from django.views.generic import ListView, DetailView

from futuregreen.news.models import *

class NewsDetailView(DetailView):
    model = Item

class NewsListView(ListView):
    model = Item