from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.images.models import Images
from apps.users.models import User


class Blog(models.Model):
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_blog')
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ForeignKey(Images, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog')
    created = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)


@receiver(post_save, sender=Blog)
@receiver(post_delete, sender=Blog)
def update_blog_list_cache(sender, instance=None, **kwargs):
    """Обновление кэша при создании/обновлении/удалении блога"""
    cache_key = 'blog_list_data'
    cache.delete(cache_key)
    queryset = Blog.objects.filter(is_active=True).values('id', 'title', 'text', 'image', 'is_active')
    data = list(queryset)
    cache.set(cache_key, data, timeout=60)
