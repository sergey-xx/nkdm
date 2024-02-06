from django.conf import settings
from mail_templated import send_mail
from blog.models import Post


def send_last_posts(user):
    """Оправка  последних 5 постов."""
    first_name = user.first_name
    posts = Post.objects.order_by('-pk')[:5]
    send_mail(
        'mail/daily_mailing.html',
        {'first_name': first_name,
         'posts': posts},
        settings.EMAIL_HOST_USER,
        [user.email]
    )
