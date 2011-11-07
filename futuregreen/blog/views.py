# blog/views.py

from django.views.generic import ArchiveIndexView, DateDetailView

from futuregreen.blog.models import *

class EntryDetailView(DateDetailView):
    queryset = Entry._default_manager.live()
    date_field="date_published"

class EntryIndexView(ArchiveIndexView):
    queryset = Entry._default_manager.live()

