# content/admin.py

from django.contrib import admin

from futuregreen.content.models import ContentBlock

admin.site.register(ContentBlock)