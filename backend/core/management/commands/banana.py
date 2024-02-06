from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from django.conf import settings

from core.emails import send_last_posts




User = get_user_model()


class Command(BaseCommand):
    """Команда для тестов и отладки."""

    help = 'Test command.'

    def handle(self, *args, **options):
        user = User.objects.first()
        send_last_posts(user)
