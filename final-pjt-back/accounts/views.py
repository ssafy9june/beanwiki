from django.shortcuts import render
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import User
from movies.models import Click, Movie, RecommendActors, RecommendKeyword, RecommendGenres 
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .serializers import UserSerializer, ClickSerializer
from django.core.serializers import serialize
from rest_framework.decorators import api_view
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# Create your views here.

@api_view(['POST'])
def userid(request):
    token = request.data['token']
    user = User.objects.get(auth_token = token)
    js = {'id' : user.id}
    data = json.dumps(js)
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request,userid):
    user = User.objects.get(id = userid)
    serializer = UserSerializer(user)
    clicks = get_list_or_404(Click, userid = userid)
    clickserializer = ClickSerializer(clicks, many=True)
    recommend_movie = recommend_main(userid)
    data = {
        'profile' : serializer.data,
        'click' : clickserializer.data,
        'recommend_movies' : recommend_movie
    }
    return Response(data)


def recommend_main(userid):
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
    return res

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def followings(request, userid):
    user = get_object_or_404(User,id=userid) # 팔로우 누르는 사람
    id = request.data['id'] # 팔로우 받는 사람
    user1 = get_object_or_404(User,id=id)
    serializer = UserSerializer(user1)
    if user != user1:
        if user.followings.filter(id = id).exists():
            user.followings.remove(user1)
        else:
            user.followings.add(user1)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def reset_algorithm(request,userid):
    id = request.data['id']
    user = get_object_or_404(User,id=userid)
    if id != userid:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    clicks = get_list_or_404(Click, userid = userid)
    for click in clicks:
        click.delete()
    movies = Movie.objects.filter(like_users=user)
    for movie in movies:
        movie.like_users.remove(user)
    return Response(status=status.HTTP_202_ACCEPTED)