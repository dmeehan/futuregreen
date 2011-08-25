# blog/admin.py

from django.contrib import admin

from blog.models import BlogEntry, BlogLink, BlogImage, LinkImage

class ImageInline(admin.StackedInline):
    model = BlogImage
    prepopulated_fields = {"slug": ("name",)}
    fields = ('image', 'is_main', 'name', 'caption',
              'crop_horz', 'crop_vert', 'slug', 'order' )
    extra = 0

    # Grappelli options
    allow_add = True
    sortable_field_name = "order"

class BlogEntryAdmin(admin.ModelAdmin):
    inlines = [
       ImageInline,
    ]


admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(BlogLink)
admin.site.register(BlogImage)
admin.site.register(LinkImage)