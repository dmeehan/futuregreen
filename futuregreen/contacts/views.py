# contacts/views.py

from django.views.generic import ListView, DetailView
from django.conf import settings

class ContactDetailView(DetailView):
    pass

class ContactListView(ListView):
    paginate_by = paginate_by = settings.CONTACT_PAGINATE_BY
    template = '/contacts/contact_list.html'
    context_object_name="contact_list",

class PersonListView(ContactListView):
    pass

class OrganizationListView(ListView):
    pass

class ContactTypeListView(ContactListView):
    pass