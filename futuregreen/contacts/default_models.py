# contacts/default_models.py

"""

        Default models for the contacts app.
        Not loaded by syncdb unless specified in settings.

"""

from models import ContactBase

class Contact(ContactBase):
    """

    Non-abstract class of ContactBase.

    """
    pass