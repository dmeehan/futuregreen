# studio/admin.py

from django.contrib import admin

from futuregreen.people.models import *

class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'employee_type', 'job_title')

admin.site.register(Client, ContactAdmin)
admin.site.register(Collaborator, ContactAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeType, ContactAdmin)
