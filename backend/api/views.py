from django.shortcuts import get_object_or_404
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from blog.models import Post, Follow, Blog, Read
from .serializers import PostSerializer
from core.tasks import schedule_task


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        blog = get_object_or_404(Blog, user=self.request.user)
        serializer.save(blog=blog)

    def list(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            queryset = Post.objects.order_by('-pk')[:500]
        else:
            queryset = Post.objects.filter(
                blog__following__user=self.request.user).order_by('-pk')[:500]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def follow_blog(request, blog_id):
    """Подписка на Блог."""
    blog = get_object_or_404(Blog, id=blog_id)
    follow = Follow.objects.filter(user=request.user,
                                   blog=blog)
    if follow.exists():
        follow.delete()
        return Response("Вы отписались",
                        status=status.HTTP_200_OK)
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
    read_post = Read.objects.filter(user=request.user,
                                    post=post)
    if read_post.exists():
        read_post.delete()
        return Response("Не прочитано",
                        status=status.HTTP_200_OK)
    read = Read.objects.create(user=request.user,
                               post=post)
    read.save()
    return Response('Прочитано',
                    status=status.HTTP_201_CREATED,)


@api_view(['POST', ])
def create_tast_send_email(request):
    schedule_task()
    return Response('Отправка сообщений активирована',
                    status=status.HTTP_201_CREATED,)
