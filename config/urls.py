
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('apps.users.urls', 'apps.users'))),
    path('images/', include(('apps.images.urls', 'apps.images'))),
    path('blogs/', include(('apps.blogs.urls', 'apps.blogs'))),
]
