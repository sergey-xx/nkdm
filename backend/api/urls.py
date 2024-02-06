from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, follow_blog, read_post, create_tast_send_email


router = DefaultRouter()

router.register('posts',
                PostViewSet,
                basename='posts')

urlpatterns = [
    path('blog/<str:blog_id>/follow/',
         follow_blog,
         name='follow_blog'),
    path('posts/<str:post_id>/read/',
         read_post,
         name='read_post'),
    path('admin/sendmails/',
         create_tast_send_email,
         name='create_tast_send_email'),

    path('', include(router.urls)),
]
