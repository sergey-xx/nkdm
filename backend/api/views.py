from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (AllowAny, IsAuthenticated,)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


from blog.models import Post, Follow, Blog, Read
from .serializers import PostSerializer
from core.tasks import send_email_task

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.order_by('-pk')[:500]
    serializer_class = PostSerializer
    http_method_names = ['get']
    permission_classes = [AllowAny,]


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def follow_blog(request, blog_id):
    """Подписка на Блог."""
    blog = get_object_or_404(Blog, id=blog_id)
    if Follow.objects.filter(user=request.user,
                             blog=blog).exists():
        return Response("Already following!",
                    status=status.HTTP_400_BAD_REQUEST)
    follow = Follow.objects.create(user=request.user,
                                   blog=blog)
    follow.save()
    return Response('Вы подписались на блог',
                    status=status.HTTP_201_CREATED,)


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def read_post(request, post_id):
    """Пометить пост прочитанным."""
    post = get_object_or_404(Post, id=post_id)
    if Read.objects.filter(user=request.user,
                           post=post).exists():
        return Response("Уже прочитан!",
                        status=status.HTTP_400_BAD_REQUEST)
    read = Read.objects.create(user=request.user,
                               post=post)
    read.save()
    return Response('Пост помечен прочитанным',
                    status=status.HTTP_201_CREATED,)

@api_view(['POST', ])
def create_tast_send_email(request):
    send_email_task.delay()
    return Response('Отправка сообщений активирована',
                    status=status.HTTP_201_CREATED,)
