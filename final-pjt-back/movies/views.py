from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Genre, Movie, Actor, Crew, Review,LikeReview, Keyword, Click, RecommendActors, RecommendGenres, RecommendKeyword
from .serializers import MovieSerializer, ReviewSerializer, ActorSerializer, CrewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
import requests
from accounts.models import User
import re
from django.core import serializers
import csv, json, random, os, bardapi
from . import recommend_algorithm, recommend_by_actors, recommend_by_genres, get_trend
from datetime import datetime
os.environ['_BARD_API_KEY'] = 'WRITE_YOUR_OWN_BARD_API_KEY'
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def find_movie_by_bard(request):
    input_text = request.data['input']
    print(input_text)
    response = bardapi.core.Bard().get_answer(input_text)
    return Response({'response' : response})

#전체 영화 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_movies(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# 개별 영화 조회, 리뷰 작성, (pk = 영화 id)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def get_movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk = pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, review_users=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data)


# 리뷰 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_like(request,reviewid):
    review = get_object_or_404(Review, id = reviewid)
    serializer = ReviewSerializer(review)
    userid = request.data['id']
    user = get_object_or_404(User, id = userid)
    if request.method == 'POST':
        if review.likes.filter(user = user).exists():
            review.likes.filter(user = user).delete()
        else:
            LikeReview.objects.create(review=review, user=user)
    return Response(serializer.data)
# 리뷰 작성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movieid):
    movie = get_object_or_404(Movie, id = movieid)
    data = request.data
    user = get_object_or_404(User, id = data['userid'])
    if not data['content']:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    review = Review.objects.create(movie = movie, review_users = user, content = data['content'])
    serializers = ReviewSerializer(review)
    return Response(serializers.data)


# 영화 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request,movieid):
    movie = get_object_or_404(Movie, id = movieid)
    data = request.data
    user = get_object_or_404(User,id = data['id'])
    if movie.like_users.filter(id = data['id']).exists():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)
# 좋아요 누른 영화 목록
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_movies(request,userid):
    user = get_object_or_404(User, id = userid)
    movies = get_list_or_404(Movie, like_users = user)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 영화 검색 - 제목
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_movies_title(request,search):
    movie = Movie.objects.filter(title__iregex= rf'{search}')
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)
# 영화 배우 검색
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_actor(request,search):
    actor = Actor.objects.filter(name__iregex= rf'{search}')
    serializer = ActorSerializer(actor, many=True)
    return Response(serializer.data)
# 영화 감독 검색
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_crew(request,search):
    crew = Crew.objects.filter(name__iregex= rf'{search}')
    serializer = CrewSerializer(crew, many=True)
    return Response(serializer.data)

# 영화 검색 - 배우
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_movies_actor(request,search):
    movie = Movie.objects.filter(actors__name__iregex= rf'{search}')
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)
#영화 검색 - 감독
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_movies_crew(request,search):
    movie = Movie.objects.filter(crews__name__iregex= rf'{search}')
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)
# 영화 검색 - 장르
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_movies_genre(request,search):
    movie = Movie.objects.filter(genres__name__iregex= rf'{search}')[:90]
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)



# 클릭시 내 추천 정보 저장
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def click(request,userid):
    data = request.data
    if not Click.objects.filter(movie_id = data['movieid'], userid = userid).exists():
        Click.objects.create(movie = Movie.objects.get(id = data['movieid']), userid = userid)
    movie = Movie.objects.get(id = data['movieid'])
    serializer = MovieSerializer(movie)
    return Response(serializer.data,status=200)








# 추천 알고리즘 모음
#메인 영화 추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_main(request, userid):
    clicks = Click.objects.filter(userid = userid)
    removie = {}
    data = []
    result = []
    for click in clicks:
        actors = RecommendActors.objects.filter(movieid = click.movie.id)
        keywords = RecommendKeyword.objects.filter(movieid = click.movie.id)
        genres = RecommendGenres.objects.filter(movieid=click.movie.id)
        for actor in actors:
            if actor.movie_title in removie:
                removie[actor.movie_title] += actor.score * 0.08
                continue
            removie[actor.movie_title] = actor.score
        for keyword in keywords:
            if keyword.movie_title in removie:
                removie[keyword.movie_title] += keyword.score * 0.08
                continue
            removie[keyword.movie_title] = keyword.score
        for genre in genres:
            if genre.movie_title in removie:
                removie[genre.movie_title] += genre.score * 0.08
                continue
            removie[genre.movie_title] = genre.score
    for movietitle,score in removie.items():
        if (movietitle,score) not in result:
            result.append((movietitle,score))
    result.sort(reverse=True, key=lambda x : x[1])
    for i in result[:90]:
        movie = Movie.objects.filter(title=i[0])[0]
        data.append({'movie': {'id': movie.id, 'title': movie.title, 'poster_path': movie.poster_path}, 'score': i[1]})
    res = json.dumps(data,ensure_ascii=False)
    return Response(res)
    
# 전체 기반 추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_movies(request, type, keyword):
    if type == 'actor':
        movie = Movie.objects.filter(actors__name__iregex= rf'{keyword}').order_by('-popularity')[:90]
        serializer = MovieSerializer(movie, many=True)
    elif type == 'genre':
        movie = Movie.objects.filter(genres__name__iregex= rf'{keyword}').order_by('-popularity')[:90]
        serializer = MovieSerializer(movie, many=True)
    elif type == 'crew':
        movie = Movie.objects.filter(crews__name__iregex= rf'{keyword}').order_by('-popularity')[:90]
        serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)

# 배우 기반 추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_actors(request, userid):
    clicks = Click.objects.filter(userid = userid)
    actor = set()
    for click in clicks:
        for act in click.movie.actors.all():
            actor.add(str(act.name))
    choice = random.choice(list(actor))
    movie = Movie.objects.filter(actors__name__iregex= rf'{choice}').order_by('-popularity')[:90]
    serializer = MovieSerializer(movie, many=True)
    data = {
        'actor': choice,
        'movies': serializer.data
    }
    return Response(data)
# 장르 기반 추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_genres(request, userid):
    clicks = Click.objects.filter(userid = userid)
    genre = set()
    for click in clicks:
        for act in click.movie.genres.all():
            genre.add(str(act.name))
    choice = random.choice(list(genre))
    movie = Movie.objects.filter(genres__name__iregex= rf'{choice}').order_by('-popularity')[:90]
    serializer = MovieSerializer(movie, many=True)
    data = {
        'genre': choice,
        'movies': serializer.data
    }
    return Response(data)
# 감독 기반 추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_crews(request, userid):
    clicks = Click.objects.filter(userid = userid)
    crew = set()
    for click in clicks:
        for act in click.movie.crews.all():
            crew.add(str(act.name))
    choice = random.choice(list(crew))
    movie = Movie.objects.filter(crews__name__iregex= rf'{choice}').order_by('-popularity')[:90]
    serializer = MovieSerializer(movie, many=True)
    data = {
        'crew': choice,
        'movies': serializer.data
    }
    return Response(data)

# 전체보기 코드
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_movies(request, type, keyword):
    if type == 'actor':
        movie = Movie.objects.filter(actors__name__iregex= rf'{keyword}').order_by('-popularity')[:90]
        serializer = MovieSerializer(movie, many=True)
    elif type == 'genre':
        movie = Movie.objects.filter(genres__name__iregex= rf'{keyword}').order_by('-popularity')[:90]
        serializer = MovieSerializer(movie, many=True)
    elif type == 'crew':
        movie = Movie.objects.filter(crews__name__iregex= rf'{keyword}').order_by('-popularity')[:90]
        serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)


# 최신 추천 영화
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_trend(request):
    result = get_trend.recommend_trend()
    return Response(result)

# 영화 기반 추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_movie(request, movieid):
    removie = {}
    data = []
    result = []
    actors = RecommendActors.objects.filter(movieid = movieid)
    keywords = RecommendKeyword.objects.filter(movieid = movieid)
    genres = RecommendGenres.objects.filter(movieid = movieid)
    for actor in actors:
        if actor.movie_title in removie:
            removie[actor.movie_title] += actor.score * 0.08
            continue
        removie[actor.movie_title] = actor.score
    for keyword in keywords:
        if keyword.movie_title in removie:
            removie[keyword.movie_title] += keyword.score * 0.08
            continue
        removie[keyword.movie_title] = keyword.score
    for genre in genres:
        if genre.movie_title in removie:
            removie[genre.movie_title] += genre.score * 0.08
            continue
        removie[genre.movie_title] = genre.score
    for movietitle,score in removie.items():
        if (movietitle,score) not in result:
            result.append((movietitle,score))
    result.sort(reverse=True, key=lambda x : x[1])
    for i in result[:15]:
        movie = Movie.objects.filter(title=i[0])[0]
        data.append({'movie': {'id': movie.id, 'title': movie.title, 'poster_path': movie.poster_path}, 'score': i[1]})
    res = json.dumps(data,ensure_ascii=False)
    return Response(res)