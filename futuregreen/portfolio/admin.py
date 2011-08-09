# futuregreen/portfolio/admin.py

from django.contrib import admin

from futuregreen.portfolio.models import Project

class ClientInline(admin.TabularInline):
    model = Project.clients.through

class CollaboratorInline(admin.TabularInline):
    model = Project.collaborators.through

class EmployeeInline(admin.TabularInline):
    model = Project.employees.through

class CategoryInline(admin.TabularInline):
    model = Project.categories.through

class ProjectAdmin(admin.ModelAdmin):
   inlines = [
       CategoryInline,
       ClientInline,
       CollaboratorInline,
       EmployeeInline,
   ]
   list_display = ('name', '-date_end')
   prepopulated_fields = {"slug": ("name",)}

admin.site.register(Project, ProjectAdmin)