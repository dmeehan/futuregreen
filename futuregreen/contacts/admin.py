# contacts/admin.py

from django.contrib import admin

from futuregreen.contacts.models import *

admin.site.register(Client)
admin.site.register(Collaborator)
admin.site.register(Employee)
admin.site.register(EmployeeType)
