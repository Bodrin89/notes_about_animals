
from django.urls import path

from apps.blogs.views import GetBlogView, CreateBlogView, ListBlogView, UpdateBlogView, DestroyBlogView
from apps.images.views import GetUrlImage

urlpatterns = [
    path('get-blog/<int:pk>/', GetBlogView.as_view(), name='get-blog'),
    path('list-blog/', ListBlogView.as_view(), name='list-blog'),
    path('create-blog/', CreateBlogView.as_view(), name='create-blog'),
    path('update-blog/<int:pk>/', UpdateBlogView.as_view(), name='update-blog'),
    path('destroy-blog/<int:pk>/', DestroyBlogView.as_view(), name='destroy-blog'),
]
