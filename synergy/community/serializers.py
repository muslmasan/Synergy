from rest_framework import serializers
from .models import Community, Comment, Post

class CommunitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Community
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'