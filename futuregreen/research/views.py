# research/views.py

from django.views.generic import ArchiveIndexView, DateDetailView, MonthArchiveView

from futuregreen.research.models import Article
from futuregreen.portfolio.models import Project

class ArticleViewMixin(View):
    queryset = Article._default_manager.live()
    date_field="date_published"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArticleViewMixin, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the projects in the research category
        context['project_list'] = Project._default_manager.live().filter(project_types__name='Research')
        return context

class ArticleDetailView(DateDetailView, ArticleViewMixin):
    pass

class ArticleIndexView(ArchiveIndexView, ArticleViewMixin):
    pass

class ArticleMonthArchiveView(MonthArchiveView, ArticleViewMixin):
    pass