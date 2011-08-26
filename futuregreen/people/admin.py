# studio/admin.py

from django.contrib import admin

from futuregreen.people.models import *

class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'employee_type', 'job_title', 'status')
    fieldsets = (
        (None, {
            'fields': ('contact_type', 'name', 'description',
                       'employee_type', 'job_title', 'status')
        }),
        ('Contact Info', {
            'classes': ('collapse closed',),
            'fields': ('address_line1', 'address_line2',
                       'city', 'state', 'code', 'country', 'email',
                       'phone', 'mobile', 'fax', 'website',)
        }),
        ('Metadata', {
            'classes': ('collapse closed',),
            'fields': ('slug',)
        }),
    )

admin.site.register(Client, ContactAdmin)
admin.site.register(Collaborator, ContactAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeType, ContactAdmin)
