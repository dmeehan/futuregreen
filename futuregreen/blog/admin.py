# blog/admin.py

from django.contrib import admin

from blog.models import BlogEntry, BlogLink, BlogImage, LinkImage

admin.site.register(BlogEntry)
admin.site.register(BlogLink)
admin.site.register(BlogImage)
admin.site.register(LinkImage)