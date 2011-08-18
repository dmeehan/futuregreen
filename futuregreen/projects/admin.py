# projects/admin.py

from django import forms
from django.contrib import admin

from easy_maps.widgets import AddressWithMapWidget

from futuregreen.projects.models import Project, ProjectImage

class ImageInline(admin.StackedInline):
    model = ProjectImage
    prepopulated_fields = {"slug": ("name",)}
    fields = ('image', 'is_main', 'name', 'caption',
              'crop_horz', 'crop_vert', 'slug', 'order' )
    extra = 0

    # Grappelli options
    allow_add = True
    sortable_field_name = "order"

class ClientInline(admin.TabularInline):
    model = Project.clients.through
    verbose_name = 'client'
    verbose_name_plural = 'clients'
    extra=1

class CollaboratorInline(admin.TabularInline):
    model = Project.collaborators.through
    verbose_name = 'collaborator'
    verbose_name_plural = 'collaborators'
    extra=1

class DesignerInline(admin.TabularInline):
    model = Project.designers.through
    verbose_name = 'designer'
    verbose_name_plural = 'designers'
    extra=1

class CategoryInline(admin.TabularInline):
    model = Project.categories.through
    verbose_name = 'category'
    verbose_name_plural = 'categories'
    extra=1

class ProjectAdmin(admin.ModelAdmin):
    class form(forms.ModelForm):
        class Meta:
            widgets = {
                'address': AddressWithMapWidget({'class': 'vTextField'})
            }
    inlines = [
       ImageInline,
       CategoryInline,
       ClientInline,
       CollaboratorInline,
       DesignerInline,
    ]
    exclude = ('clients', 'collaborators', 'designers', 'categories',)
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)



