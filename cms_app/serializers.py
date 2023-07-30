from rest_framework import serializers
from .models import Post, Like
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username",)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField(read_only=True) 
    owner = UserSerializer(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ('owner',)

    def get_likes_count(self, obj):
        return obj.likes.count() 

    def get_likes(self, obj):
        likes = LikeSerializer(Like.objects.filter(post=obj), many=True).data  
        return likes


