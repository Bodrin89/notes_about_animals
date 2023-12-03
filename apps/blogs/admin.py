from django.contrib import admin

from apps.blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
