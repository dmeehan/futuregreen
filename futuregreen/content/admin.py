# content/admin.py

from django.contrib import admin

from futuregreen.content.models import ContentBlock

class ContentBlockAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Title', {
            'fields': ('title',)
        }),
        ('Text', {
            'fields': ('excerpt', 'body',)
        }),
        ('Image', {
            'fields': ('image', 'crop_vert', 'crop_horz')
        }),
    )

admin.site.register(ContentBlock, ContentBlockAdmin)