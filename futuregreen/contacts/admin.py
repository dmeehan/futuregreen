# contacts/admin.py

from django.contrib import admin

from futuregreen.contacts.models import *

class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Client, ContactAdmin)
admin.site.register(Collaborator, ContactAdmin)
admin.site.register(Employee, ContactAdmin)
admin.site.register(EmployeeType, ContactAdmin)
