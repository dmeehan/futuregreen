# contacts/views.py

from django.views.generic import ListView, DetailView

#from contacts.settings import CONTACT_PAGINATE_BY

class ContactDetailView(DetailView):
    pass
    #model = contact_model

class ContactListView(ListView):
    pass
    #model = contact_model
    #paginate_by = paginate_by = CONTACT_PAGINATE_BY
    #template = '/contacts/contact_list.html'
    #context_object_name="contact_list",

class PersonListView(ContactListView):
    pass
    #queryset = contact_model.objects.people()

class OrganizationListView(ListView):
    pass
    #queryset = contact_model.objects.organizations()

class ContactTypeListView(ContactListView):
    pass
    #queryset = contact_model.objects.people()