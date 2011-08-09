# futuregreen/portfolio/admin.py

from django.contrib import admin

from futuregreen.portfolio.models import Project

class ClientInline(admin.TabularInline):
    model = Project.clients.through
    verbose_name = 'client'
    verbose_name_plural = 'clients'

class CollaboratorInline(admin.TabularInline):
    model = Project.collaborators.through
    verbose_name = 'collaborator'
    verbose_name_plural = 'collaborators'
    extra=0

class DesignerInline(admin.TabularInline):
    model = Project.designers.through
    verbose_name = 'designer'
    verbose_name_plural = 'designers'
    extra=0

class CategoryInline(admin.TabularInline):
    model = Project.categories.through
    verbose_name = 'category'
    verbose_name_plural = 'categories'
    extra=0

class ProjectAdmin(admin.ModelAdmin):
   inlines = [
       ClientInline,
       CollaboratorInline,
       DesignerInline,
       CategoryInline,
   ]
   exclude = ('clients', 'collaborators', 'employees', 'categories',)
   list_display = ('name',)
   prepopulated_fields = {"slug": ("name",)}

admin.site.register(Project, ProjectAdmin)