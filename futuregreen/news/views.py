# news/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, ArchiveIndexView

from futuregreen.news.models import NewsItem
from futuregreen.people.models import Employee
from futuregreen.portfolio.models import Project

class NewsDetailView(DetailView):
    model = NewsItem.objects.live()

class NewsListView(ListView):
    queryset = NewsItem.objects.live()

class NewsIndexView(ArchiveIndexView):
    queryset = NewsItem.objects.live()
    date_field="date_published"
    
    #context_object_name = "news_list"
    #template_name = "news/newsitem_list.html"
