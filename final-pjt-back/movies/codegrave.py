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
import csv, json
from . import recommend_algorithm, recommend_by_actors, recommend_by_genres












#영화 추천
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def recommend_keywords(request,search): # 함수 사용
    data = recommend_algorithm.recommend(search)
    return Response(data)
@api_view(['GET'])
def recommend_genres(request,search): # 장르기반 추천
    data = recommend_by_genres.recommend(search)
    return Response(data)
@api_view(['GET'])
def recommend_actors(request,search): # 배우기반 추천
    data = recommend_by_actors.recommend(search)
    return Response(data)

@api_view(['GET'])
def make_recommend(request):
    RecommendKeyword.objects.all().delete()
    RecommendGenres.objects.all().delete()
    RecommendActors.objects.all().delete()
    movies = Movie.objects.all()
    for movie in movies:
        data_keywords = recommend_algorithm.recommend(movie.title)
        data_genres = recommend_by_genres.recommend(movie.title)
        data_actors = recommend_by_actors.recommend(movie.title)
        for data in data_keywords:
            RecommendKeyword.objects.create(movieid = movie.id, movie = Movie.objects.get(id=data['id']), origin = movie.title, movie_title = data['title'], score = float(data['score']))
        for data in data_genres:
            RecommendGenres.objects.create(movieid = movie.id, movie = Movie.objects.get(id=data['id']), origin = movie.title, movie_title = data['title'], score = float(data['score']))
        for data in data_actors:
            RecommendActors.objects.create(movieid = movie.id, movie = Movie.objects.get(id=data['id']), origin = movie.title, movie_title = data['title'], score = float(data['score']))
    return 1
#영화 추천 알고리즘
def export_movies_csv(request):
    # Define the file path to save the CSV file
    file_path = 'movies.csv'

    # Define the field names for the CSV file
    field_names = ['id', 'title', 'release_date', 'popularity', 'vote_count', 'vote_average', 'overview', 'poster_path', 'youtube_key', 'genres','keywords', 'actors']
    # field_names = ['id', 'title', 'popularity', 'vote_count', 'vote_average', 'poster_path', 'youtube_key', 'genres','keywords', 'actors']
    sametitle = set()
    # Get the movies data from the database
    movies = Movie.objects.all()

    # Create a new CSV file and write the data
    with open(file_path, mode='w', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(field_names)

        # Iterate over each movie and write its data to the CSV file
        for movie in movies:
            if movie.title in sametitle:
                continue
            sametitle.add(movie.title)
            # Get the genres for the current movie
            genres = movie.genres.all()
            keywords = movie.keywords.all()
            actors = movie.actors.all()
            genre_data = [{'id': genre.id, 'name': genre.name} for genre in genres]
            genre_json = json.dumps(genre_data, ensure_ascii=False)  # Ensure ASCII=False to preserve non-ASCII characters
            keyword_data = [{'id': keyword.id, 'name': keyword.name} for keyword in keywords]
            keyword_json = json.dumps(keyword_data, ensure_ascii=False)  # Ensure ASCII=False to preserve non-ASCII characters
            actors_data = [{'id': actors.id, 'name': ''.join(actors.name.split())} for actors in actors]
            actors_json = json.dumps(actors_data, ensure_ascii=False)  # Ensure ASCII=False to preserve non-ASCII characters
            
            row = [
                movie.id,
                movie.title,
                movie.release_date,
                movie.popularity,
                movie.vote_count,
                movie.vote_average,
                movie.overview,
                movie.poster_path,
                movie.youtube_key,
                genre_json,
                keyword_json,
                actors_json,
            ]
            writer.writerow(row)

    # Provide the CSV file for download
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="movies.csv"'

    return response









#클릭 대표 영화
def click_csv(request, user_id):
    # Define the file path to save the CSV file
    file_path = 'clicks.csv'

    # Define the field names for the CSV file
    field_names = ['id', 'title', 'release_date', 'popularity', 'vote_count', 'vote_average', 'overview', 'poster_path', 'youtube_key', 'genres','keywords']

    # Get the movies data from the database
    clicks = Click.objects.filter(userid = user_id)
    temp = []
    for click in clicks:
        temp.append(click.movie)
    # Create a new CSV file and write the data
    with open(file_path, mode='w', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(field_names)

        # Iterate over each movie and write its data to the CSV file
        for click in temp:
            # Get the genres for the current movie
            genres = click.genres.all()
            keywords = click.keywords.all()
            genre_data = [{'id': genre.id, 'name': genre.name} for genre in genres]
            genre_json = json.dumps(genre_data, ensure_ascii=False)  # Ensure ASCII=False to preserve non-ASCII characters
            keyword_data = [{'id': keyword.id, 'name': keyword.name} for keyword in keywords]
            keyword_json = json.dumps(keyword_data, ensure_ascii=False)  # Ensure ASCII=False to preserve non-ASCII characters

            row = [
                click.id,
                click.title,
                click.release_date,
                click.popularity,
                click.vote_count,
                click.vote_average,
                click.overview,
                click.poster_path,
                click.youtube_key,
                genre_json,
                keyword_json
            ]
            writer.writerow(row)

    # Provide the CSV file for download
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="clicks.csv"'
    score = {}
    for tem in temp:
        results = recommend_algorithm.csv_recommend(tem.title)
        for result in results:
            print(result)
            if result.get('title') in score:
                score[result.get('title')] += float(result.get('score')) * 0.08
            else:
                score[result.get('title')] = float(result.get('score'))
    most_movie = ''
    _max = 0
    for title,score in score.items():
        if score > _max:
            _max = score
            most_movie = title
    print(most_movie, _max)
    return recommend_movies(request,most_movie)

















# DB 생성
# TMDB API KEY 작성




API_KEY = 'WRITE_YOUR_OWN_API_KEY'

GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'

def tmdb_genres():
    response = requests.get(
        GENRE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-KR',            
        }
    ).json()    
    for genre in response.get('genres'):
        if Genre.objects.filter(pk=genre['id']).exists(): continue        
        print(genre)
        Genre.objects.create(
            id=genre['id'],
            name=genre['name']
        )
    return JsonResponse(response)


def get_youtube_key(movie_dict):    
    movie_id = movie_dict.get('id')
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
        params={
            'api_key': API_KEY
        }
    ).json()
    for video in response.get('results'):
        if video.get('site') == 'YouTube':
            return video.get('key')
    return 'nothing'

def get_actors(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()

    for person in response.get('cast'):
        if person.get('known_for_department') != 'Acting': continue
        actor_id = person.get('id')
        if not Actor.objects.filter(pk=actor_id).exists():
            actor = Actor.objects.create(
                id=person.get('id'),
                name=person.get('name'),
                profile_path = person.get('profile_path'),
                popularity = person.get('popularity')
                
            )
        movie.actors.add(actor_id)
        if movie.actors.count() == 5:
            break
def get_crews(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()

    for person in response.get('crew'):
        if person.get('job') != 'Director': continue
        actor_id = person.get('id')
        if not Crew.objects.filter(pk=actor_id).exists():
            crew = Crew.objects.create(
                id=person.get('id'),
                name=person.get('name'),
                profile_path = person.get('profile_path'),
                popularity = person.get('popularity')
            )
        movie.crews.add(actor_id)
        if movie.crews.count() == 1:
            break

def get_keywords(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/keywords',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()

    for keyword in response.get('keywords'):
        keyword_id = keyword.get('id')
        if not Keyword.objects.filter(pk=keyword_id).exists():
            keywords = Keyword.objects.create(
                id=keyword.get('id'),
                name=keyword.get('name'),
            )
        movie.keywords.add(keyword_id)
temp = set()
def movie_data(page=1):
    global a, temp
    response = requests.get(
        POPULAR_MOVIE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',     
            'page': page,       
        }
    ).json()

    for movie_dict in response.get('results'):
        if not movie_dict.get('release_date'): continue   # 없는 필드 skip
        # 유투브 key 조회
        youtube_key = get_youtube_key(movie_dict)
        if movie_dict.get('id') in temp :
            print(movie_dict.get('id'), '여기에요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            continue
        temp.add(movie_dict.get('id'))
        movie = Movie.objects.create(
            id=movie_dict.get('id'),
            title=movie_dict.get('title'),
            release_date=movie_dict.get('release_date'),
            popularity=movie_dict.get('popularity'),
            vote_count=movie_dict.get('vote_count'),
            vote_average=movie_dict.get('vote_average'),
            overview=movie_dict.get('overview'),
            poster_path=movie_dict.get('poster_path'),   
            youtube_key=youtube_key,       
        )
        for genre_id in movie_dict.get('genre_ids', []):
            movie.genres.add(genre_id)

        # 배우들 저장
        get_actors(movie)
        get_crews(movie)
        get_keywords(movie)
        print('>>>', movie.title, '==>', movie.youtube_key, a)
        a += 1

def tmdb_data(request):
    Genre.objects.all().delete()
    Actor.objects.all().delete()
    Movie.objects.all().delete()
    Crew.objects.all().delete()
    Keyword.objects.all().delete()

    tmdb_genres()
    for i in range(1,500):
        movie_data(i)
    return HttpResponse('OK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')