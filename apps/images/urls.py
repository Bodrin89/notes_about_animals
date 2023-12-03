from django.urls import path

from apps.images.views import GetUrlImage

urlpatterns = [
    path('search-images/', GetUrlImage.as_view(), name='search-images'),
]