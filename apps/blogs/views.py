
from django.core.cache import cache
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from apps.blogs.models import Blog
from apps.blogs.permissions import OwnerPermission
from apps.blogs.serializers import GetBlogSerializer, CreateBlogSerializer, UpdateBlogSerializer


class GetBlogView(generics.RetrieveAPIView):
    """Получить блог по id"""
    serializer_class = GetBlogSerializer
    queryset = Blog.objects.filter(is_active=True)


class ListBlogView(generics.ListAPIView):
    """Получить все блоги"""
    serializer_class = GetBlogSerializer
    queryset = Blog.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        cached_data = cache.get('blog_list_data')
        if cached_data is not None:
            return Response(cached_data)

        queryset = Blog.objects.filter(is_active=True)
        serializer = self.serializer_class(queryset, many=True)
        data = serializer.data

        cache.set('blog_list_data', data, timeout=60)

        return Response(data)


class CreateBlogView(generics.CreateAPIView):
    """Создать новый блог"""
    serializer_class = CreateBlogSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateBlogView(generics.UpdateAPIView):
    """Обновить блог"""
    serializer_class = UpdateBlogSerializer
    permission_classes = [permissions.IsAuthenticated, OwnerPermission]
    queryset = Blog.objects.all()


class DestroyBlogView(generics.DestroyAPIView):
    """Удалить блог"""
    permission_classes = [permissions.IsAuthenticated, OwnerPermission]
    queryset = Blog.objects.all()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        return Response('Блог удален')
