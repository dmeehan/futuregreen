# portfolio/admin.py

from django import forms
from django.contrib import admin

from easy_maps.widgets import AddressWithMapWidget

from futuregreen.portfolio.models import Project, ProjectImage

class ProjectImageAdmin(admin.ModelAdmin):
    model = ProjectImage
    list_display = ('name', 'admin_thumbnail_view', 'project')
    prepopulated_fields = {"slug": ("name",)}

    ordering = ('project',)

class ImageInline(admin.StackedInline):
    model = ProjectImage
    fieldsets = (
        (None, {
            'fields': ('image', 'name', 'caption',),
        }),
        (None, {
            'classes': ('collapse closed',),
            'fields': ('is_main', 'crop_horz', 'crop_vert', 'slug', 'order')
        }),
    )
    prepopulated_fields = {"slug": ("name",)}
    extra = 1

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

class BuilderInline(admin.TabularInline):
    model = Project.builders.through
    verbose_name = 'builder'
    verbose_name_plural = 'builders'
    extra=1

class ProjectAdmin(admin.ModelAdmin):
    class form(forms.ModelForm):
        class Meta:
            widgets = {
                'address': AddressWithMapWidget({'class': 'vTextField'})
            }
            
    inlines = [
       ImageInline,
       ClientInline,
       CollaboratorInline,
       DesignerInline,
       BuilderInline,
    ]

    fieldsets = (
        (None, {
            'classes': ('collapse open',),
            'fields': ('name', 'short_description',
                       'description', 'external_url')
        }),
        (None, {
            'classes': ('collapse open',),
            'fields': ('tags', 'date_start', 'date_end',
                       'area', 'unit', 'address',)
        }),
        ('Metadata', {
            'classes': ('collapse open',),
            'fields': ('status', 'slug', 'user',)
        }),
    )
    list_display = ('name', 'date_end', 'area_normalized', 'status', 'featured')
    list_editable = ('status', 'featured')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)



