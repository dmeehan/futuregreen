# portfolio/admin.py

from django import forms
from django.contrib import admin

from easy_maps.widgets import AddressWithMapWidget
from categories.admin import CategoryAdmin

from futuregreen.portfolio.models import Project, ProjectImage, ProjectType, LandscapeType

class ProjectImageAdmin(admin.ModelAdmin):
    model = ProjectImage
    list_display = ('name', 'admin_thumbnail_view', 'project')

    ordering = ('project',)

class ImageInline(admin.StackedInline):
    model = ProjectImage
    fields = ('image', 'name', 'caption',
              'is_main', 'crop_horz', 'crop_vert', 'order',)
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

class BuilderInline(admin.TabularInline):
    model = Project.builders.through
    verbose_name = 'builder'
    verbose_name_plural = 'builders'
    extra=1

class ProjectTypeInline(admin.TabularInline):
    model = Project.project_types.through
    verbose_name = 'project type'
    verbose_name_plural = 'project types'
    extra=1

class LandscapeTypeInline(admin.TabularInline):
    model = Project.landscape_types.through
    verbose_name = 'landscape type'
    verbose_name_plural = 'landscape types'
    extra=1

class ProjectAdmin(admin.ModelAdmin):
    class form(forms.ModelForm):
        class Meta:
            widgets = {
                'address': AddressWithMapWidget({'class': 'vTextField'})
            }
            
    inlines = [
       ImageInline,
       ProjectTypeInline,
       LandscapeTypeInline,
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
            'classes': ('collapse closed',),
            'fields': ('status', 'slug', 'user',)
        }),
    )

    list_display = ('name', 'date_end', 'area_normalized', 'status', 'featured')
    list_editable = ('status', 'featured')
    list_filter = ( 'featured', 'status', 'project_types',
                    'landscape_types', 'clients', 'collaborators',
                    'designers', 'builders')
    search_fields = ['name', 'description', 'designers__name',
                     'builders__name', 'clients__name', 'collaborators__name',]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(ProjectType, CategoryAdmin)
admin.site.register(LandscapeType, CategoryAdmin)


