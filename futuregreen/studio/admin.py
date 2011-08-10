# futuregreen/studio/admin.py

from django.contrib import admin

from futuregreen.studio.models import Client, Collaborator, Employee, EmployeeType

class EmployeeTypeAdmin(admin.ModelAdmin):
   list_display = ('name', 'description')
   prepopulated_fields = {"slug": ("name",)}

class EmployeeAdmin(admin.ModelAdmin):
   list_display = ('name', 'job_title')
   prepopulated_fields = {"slug": ("name",)}
   exclude = ('contact_type')

class ContactAdmin(admin.ModelAdmin):
   list_display = ('name',)
   prepopulated_fields = {"slug": ("name",)}

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Client, ContactAdmin)
admin.site.register(Collaborator, ContactAdmin)
admin.site.register(EmployeeType, EmployeeTypeAdmin)
