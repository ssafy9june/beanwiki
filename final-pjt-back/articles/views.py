from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Article, Comment
from accounts.models import User
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# 토큰까지 확인 할건가>>




# article 목록 보기
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def articles(request):
    article = get_list_or_404(Article)
    serializer = ArticleSerializer(article,many=True)
    return Response(serializer.data)

# article 작성
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def article(request,userid):
    user = get_object_or_404(User, id=userid)
    if request.method == 'POST':
        data = request.data
        article = Article.objects.create(title = data['title'], content = data['content'], user=user)
        serialzer = ArticleSerializer(article)
        return Response(serialzer.data)
    elif request.method == 'DELETE':
        data = request.data
        article = get_object_or_404(Article,id=data['id'])
        if article.user == user:
            result = {'response' : '삭제되었습니다', 'title' : article.title}
            article.delete()
            return Response(result)
        result = {'response' : '작성 유저가 아닙니다'}
        return Response(result, status=status.HTTP_401_UNAUTHORIZED)
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def comment(request,userid):
    user = get_object_or_404(User, id=userid)
    if request.method == 'POST':
        data = request.data
        article = get_object_or_404(Article, id = data['id'])
        comment = Comment.objects.create(article = article, content = data['content'], user = user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        data = request.data
        comment = get_object_or_404(Comment, id=data['id'])
        if comment.user == user:
            comment.delete()
            return Response({'response' : '댓글 삭제 완료'})
        return Response({'response' : '댓글 작성자가 아닙니다'},status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_article(request,userid):
    user = get_object_or_404(User, id=userid)
    data = request.data
    article = get_object_or_404(Article, id = data['id'])
    if article.likeuser.filter(id=userid).exists():
        article.likeuser.remove(user)
    else:
        article.likeuser.add(user)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

