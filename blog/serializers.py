from dataclasses import fields
from rest_framework import serializers

from blog.models import Article as ArticleModel
from blog.models import ArticleComment as ArticleCommentModel
from blog.models import Like as LikeModel


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    updated_time = serializers.SerializerMethodField()

    def get_username(self,obj):
        return obj.user.fullname

    def get_updated_time(self, obj):
        updated_time = obj.updated_at.replace(microsecond=0).isoformat()
        return updated_time
    
    class Meta:
        model = ArticleCommentModel
        # fields = "__all__"
        fields = ["id", "article", "comment", "user", "username",
                  "created_at","updated_at", "updated_time"]


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source="comment_set")
    likes = LikeSerializer(many=True, read_only=True, source="like_set")
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.fullname

    class Meta:
        model = ArticleModel
        # fields = "__all__"
        fields = ["id", "username", "user", "title", "content",
                  "comments", "likes", "created_at", "updated_at",]