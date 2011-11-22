# research/views.py

from django.views.generic import ArchiveIndexView, DateDetailView

from futuregreen.research.models import Article

class ArticleyDetailView(DateDetailView):
    queryset = Article._default_manager.live()
    date_field="date_published"

class ArticleIndexView(ArchiveIndexView):
    queryset = Article._default_manager.live()
    date_field="date_published"