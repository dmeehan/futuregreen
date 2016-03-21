# publications/views.py

from django.views.generic import TemplateView

from .models import Publication

class PublicationView(TemplateView):
    template_name = 'book.html'

    def get_context_data(self, **kwargs):
        return {'book': Publication.objects.all()[0] }



