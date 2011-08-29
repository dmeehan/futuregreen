# news/admin.py

from django.contrib import admin

from futuregreen.news.models import Item, ItemImage

class ImageInline(admin.StackedInline):
    model = ItemImage
    prepopulated_fields = {"slug": ("name",)}
    fields = ('image', 'name', 'caption',
              'is_main', 'crop_horz', 'crop_vert', 'order' )
    extra = 0

    # Grappelli options
    allow_add = True
    sortable_field_name = "order"

class ItemAdmin(admin.ModelAdmin):
    inlines = [
       ImageInline,
    ]

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage)