from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Blog

User = get_user_model()


@receiver(post_save, sender=User)
def client_notification(sender, instance, created, **kwargs):
    """Создает Блог новому пользователю."""
    if not Blog.objects.filter(user=instance).exists():
        blog = Blog.objects.create(user=instance)
        blog.save()
