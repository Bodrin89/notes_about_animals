from django.contrib import admin

from apps.images.models import Images


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass
