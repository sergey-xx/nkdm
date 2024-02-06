from rest_framework import serializers

from blog.models import Post, Read


class PostSerializer(serializers.ModelSerializer):

    is_read = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'pub_date', 'is_read',)
        read_only_fields = ('id', 'is_read', 'pub_date')

    def get_is_read(self, post):
        user = self.context.get('request').user
        if not user.is_anonymous:
            if Read.objects.filter(post=post,
                                   user=user).exists():
                return True
        return False
