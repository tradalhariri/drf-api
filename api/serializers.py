from rest_framework import serializers

from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'created_at', 'updated_at','published','author')