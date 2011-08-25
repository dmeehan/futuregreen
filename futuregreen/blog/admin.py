# blog/admin.py

from django.contrib import admin

from futuregreen.blog.models import Entry, Link, EntryImage, LinkImage

class ImageInline(admin.StackedInline):
    model = EntryImage
    prepopulated_fields = {"slug": ("name",)}
    fields = ('image', 'is_main', 'name', 'caption',
              'crop_horz', 'crop_vert', 'slug', 'order' )
    extra = 0

    # Grappelli options
    allow_add = True
    sortable_field_name = "order"

class EntryAdmin(admin.ModelAdmin):
    inlines = [
       ImageInline,
    ]

admin.site.register(Entry, EntryAdmin)
admin.site.register(Link)
admin.site.register(EntryImage)
admin.site.register(LinkImage)