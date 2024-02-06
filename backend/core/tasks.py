from time import sleep
from django.core.mail import send_mail
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from celery import shared_task


@shared_task()
def send_email_task():
        """Sends an email when the feedback form has been submitted."""
        # sleep(2)  # Simulate expensive operation(s) that freeze Django
        send_mail(subject="Your Feedback",
                  recipient_list=['mcpali4@mail.ru'],
                  from_email='mcpali4@mail.ru',
                  fail_silently=False,
                  message='Banana message'
                  )


def schedule_task():
        interval, _ = IntervalSchedule.objects.get_or_create(
                every=30,
                period=IntervalSchedule.SECONDS
        )
        PeriodicTask.objects.create(
                interval=interval,
                name='send_emails',
                task='core.tasks.send_email_task'
        )
