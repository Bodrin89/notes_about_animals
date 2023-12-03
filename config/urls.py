
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('apps.users.urls', 'apps.users'))),
    path('images/', include(('apps.images.urls', 'apps.images'))),
    path('blogs/', include(('apps.blogs.urls', 'apps.blogs'))),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]
