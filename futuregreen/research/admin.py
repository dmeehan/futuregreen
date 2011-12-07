# research/admin.py

from django.contrib import admin

from futuregreen.research.models import Article, ArticleImage, ArticleProject, ArticleFile

class ImageInline(admin.StackedInline):
    model = ArticleImage
    fields = ('image', 'name', 'caption',
              'is_main', 'crop_horz', 'crop_vert', 'order' )
    extra = 0

    # Grappelli options
    allow_add = True
    sortable_field_name = "order"

class ProjectInline(admin.StackedInline):
    model = ArticleProject
    extra = 0

    # Grappelli options
    allow_add = True

class FileInline(admin.StackedInline):
    model = ArticleFile
    extra = 0

    # Grappelli options
    allow_add = True

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
       ImageInline,
       FileInline,
       ProjectInline,
    ]

    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article, ArticleAdmin)