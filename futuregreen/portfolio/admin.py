# futuregreen/portfolio/admin.py

from django.contrib import admin

from futuregreen.portfolio.models import Project

class ClientInline(admin.TabularInline):
    model = Project.clients.through

class CollaboratorInline(admin.TabularInline):
    model = Project.collaborators.through

class DesignerInline(admin.TabularInline):
    model = Project.designers.through

class ProjectAdmin(admin.ModelAdmin):
   inlines = [
       ClientInline,
       CollaboratorInline,
       DesignerInline,
   ]
   list_display = ('name', '-date_end')
   prepopulated_fields = {"slug": ("name",)}

admin.site.register(Project, ProjectAdmin)