# contacts/urls.py

from django.conf.urls.defaults import *

from contacts.views import *
from contacts.models import *

urlpatterns = patterns('',
    url(r'^contacts/$', 'ContactListView.as_view()', name="contacts_contact_list" ),
    url(r'^contacts/people/$', 'PersonListView.as_view()', name="contacts_person_list" ),
    url(r'^contacts/organizations/$', 'OrganizationListView.as_view()', name="contacts_organization_list" ),
    url(r'^contacts/(?P<type>[-\w]+)/$', 'ContactTypeListView.as_view()', name="contacts_type_list" ),
    url(r'^contacts/contact/(?P<slug>[-\w]+)/$', 'ContactDetailView.as_view()', name="contacts_contact_detail" ),
)