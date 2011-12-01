# studio/admin.py

from django.contrib import admin

from futuregreen.studio.models import NewsItem, NewsItemImage, NewsItemProject, NewsItemFile

class NewsImageInline(admin.StackedInline):
    model = NewsItemImage
    fields = ('image', 'name', 'caption',
              'is_main', 'crop_horz', 'crop_vert', 'order' )
    extra = 0

    # Grappelli options
    allow_add = True
    sortable_field_name = "order"

class ProjectInline(admin.StackedInline):
    model = NewsItemProject
    extra = 0

    # Grappelli options
    allow_add = True

class FileInline(admin.StackedInline):
    model = NewsItemFile
    extra = 0

    # Grappelli options
    allow_add = True

class NewsItemAdmin(admin.ModelAdmin):
    inlines = [
       NewsImageInline,
       ProjectInline,
       FileInline
    ]

    prepopulated_fields = {"slug": ("title",)}

admin.site.register(NewsItem, NewsItemAdmin)