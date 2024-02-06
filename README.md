# nkdm

celery -A nkdm  beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler