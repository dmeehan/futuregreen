# publications/admin.py

from django.contrib import admin

from .models import Publication, PublicationLink

class PublicationLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'order',]
    list_editable = ['order',]

class PublicationLinkInlineAdmin (admin.TabularInline):
    model = PublicationLink

class PublicationAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}
    inlines = [ PublicationLinkInlineAdmin ]

admin.site.register(PublicationLink, PublicationLinkAdmin)
admin.site.register(Publication, PublicationAdmin)