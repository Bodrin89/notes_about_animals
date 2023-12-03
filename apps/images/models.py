
from django.db import models

from apps.users.models import User


class Images(models.Model):
    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id: {self.id} title: {self.title}"

