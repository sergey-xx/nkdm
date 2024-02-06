import random
import string

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from django.conf import settings
from blog.models import Blog, Post


User = get_user_model()

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def generate_users(amount):
    for i in range(amount):
        username = get_random_string(5)
        first_name = get_random_string(5)
        last_name = get_random_string(5)
        email = get_random_string(5) + '@' + '.com'
        password = get_random_string(10)
        users = []
        if not User.objects.filter(username=username):
            users.append(User(username=username,
                                first_name=first_name,
                                last_name=last_name,
                                password=password,
                                email=email))
            User.objects.bulk_create(users)


def generate_post(blog, amount):
    posts = []
    for i in range(amount):
        posts.append(Post(title=get_random_string(50),
                          text=get_random_string(150),
                          blog=blog))
    Post.objects.bulk_create(posts)


class Command(BaseCommand):
    """Команда для генерации данных."""

    help = 'Generate test data command.'

    def add_arguments(self, parser):
        parser.add_argument("amount", nargs="+", type=int)

    def handle(self, *args, **options):
        amount = options['amount'][0]
        generate_users(amount)

        blogs = Blog.objects.all()
        for blog in blogs:
            generate_post(blog, amount)
