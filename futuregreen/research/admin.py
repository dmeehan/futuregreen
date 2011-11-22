# blog/admin.py

from django.contrib import admin

from futuregreen.research.models import Article, ArticleImage

class ImageInline(admin.StackedInline):
    model = ArticleImage
    fields = ('image', 'name', 'caption',
              'is_main', 'crop_horz', 'crop_vert', 'order' )
    extra = 0

    # Grappelli options
    allow_add = True
    sortable_field_name = "order"

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
       ImageInline,
    ]

    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article, ArticleAdmin)