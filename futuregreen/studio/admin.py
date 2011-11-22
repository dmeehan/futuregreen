# studio/admin.py

from django.contrib import admin

from futuregreen.studio.models import NewsItem, NewsItemImage

class NewsImageInline(admin.StackedInline):
    model = NewsItemImage
    fields = ('image', 'name', 'caption',
              'is_main', 'crop_horz', 'crop_vert', 'order' )
    extra = 0

    # Grappelli options
    allow_add = True
    sortable_field_name = "order"

class NewsItemAdmin(admin.ModelAdmin):
    inlines = [
       NewsImageInline,
    ]

    prepopulated_fields = {"slug": ("title",)}

admin.site.register(NewsItem, NewsItemAdmin)