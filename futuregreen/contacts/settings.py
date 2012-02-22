# contacts/settings.py

from django.conf import settings

DEFAULT_SETTINGS = {
    'CONTACT_MODEL': 'contacts.default_models.Contact',
    'CONTACT_MARKUP': '',
    'CONTACT_PAGINATE_BY': 10,
}

DEFAULT_SETTINGS.update(getattr(settings, 'CONTACTS_SETTINGS', {}))

# Add all the keys/values to the module's namespace
globals().update(DEFAULT_SETTINGS)