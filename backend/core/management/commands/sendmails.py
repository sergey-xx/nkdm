from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from core.tasks import schedule_task

User = get_user_model()


class Command(BaseCommand):
    """Команда для тестов и отладки."""

    help = 'Test command.'

    def handle(self, *args, **options):
        schedule_task()
    print('Отправка сообщений активирована')
