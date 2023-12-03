from django.utils import timezone

from apps.blogs.models import Blog
from config.celery import app


@app.task
def del_old_blog():
    """Удаление старых блогов из БД"""
    thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
    Blog.objects.filter(is_active=False, created__lte=thirty_days_ago).delete()
