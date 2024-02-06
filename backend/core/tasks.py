from django.contrib.auth import get_user_model
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from celery import shared_task
from core.emails import send_last_posts
from django.conf import settings

User = get_user_model()


@shared_task()
def daily_task():
    users = User.objects.all()
    for user in users:
        send_last_posts(user)


def schedule_task():
    interval, _ = (IntervalSchedule.objects.get_or_create(
          every=settings.EMAIL_SENDING_PERIOD,
          period=IntervalSchedule.DAYS))
    PeriodicTask.objects.create(interval=interval,
                                name='send_emails',
                                task='core.tasks.daily_task')
