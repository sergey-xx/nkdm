from django.contrib import admin

from .models import Blog, Post, Follow, Read


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    pass


@admin.register(Read)
class ReadAdmin(admin.ModelAdmin):
    pass
