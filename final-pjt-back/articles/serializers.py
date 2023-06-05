from rest_framework import serializers
from .models import Article, Comment
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username',)

class CommentSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True,source='user')
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('writer', )


class ArticleSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True,source='user')
    comment = CommentSerializer(many=True,read_only=True,source='article_comment')
    class Meta:
        model = Article
        fields = ('id','title','content','comment','writer','likeuser','created_at','updated_at')
        
