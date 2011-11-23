# research/views.py

from django.views.generic import ArchiveIndexView, DateDetailView

from futuregreen.research.models import Article
from futuregreen.portfolio.models import Project

class ArticleDetailView(DateDetailView):
    queryset = Article._default_manager.live()
    date_field="date_published"

class ArticleIndexView(ArchiveIndexView):
    queryset = Article._default_manager.live()
    date_field="date_published"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArticleIndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the projects in the research category
        context['project_list'] = Project._default_manager.filter(project_types__name='Research', status=Project.STATUS_LIVE)
        return context