from rest_framework.response import Response
import requests
import json
from .models import Genre


API_KEY = 'WRITE_YOUR_OWN_API_KEY'
TREND_MOVIE_URL = 'https://api.themoviedb.org/3/trending/movie/week'
GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'

def recommend_trend():
    result = []
    def get_trend(page=1):
        response = requests.get(
            TREND_MOVIE_URL,
            params={
                'api_key':'WRITE_YOUR_OWN_API_KEY',
                'language': 'ko-kr',   
                'page': page,       
            }
        ).json()
        result.append(response)
    for i in range(1,6):
        get_trend(i)
    res = json.dumps(result,ensure_ascii=False)
    return res


# def get_youtube_key(movie_dict):    
#     movie_id = movie_dict.get('id')
#     response = requests.get(
#         f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
#         params={
#             'api_key': API_KEY
#         }
#     ).json()
#     for video in response.get('results'):
#         if video.get('site') == 'YouTube':
#             return video.get('key')
#     return 'nothing'

# def get_actors(movie_dict):
#     actors = []
#     movie_id = movie_dict.get('id')
#     response = requests.get(
#         f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',
#         }
#     ).json()

#     for person in response.get('cast'):
#         if person.get('known_for_department') != 'Acting': continue
#         actor_id = person.get('id')
#         name=person.get('name'),
#         profile_path = person.get('profile_path'),
#         actors.append({'actor_id': actor_id, 'name' : name, 'profile_path' : profile_path})
#         if len(actors) == 5:
#             break
#     return actors
# def get_crews(movie_dict):
#     crews = []
#     movie_id = movie_dict.get('id')
#     response = requests.get(
#         f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',
#         }
#     ).json()

#     for person in response.get('crew'):
#         if person.get('job') != 'Director': continue
#         actor_id = person.get('id')
#         name=person.get('name'),
#         profile_path = person.get('profile_path'),
#         crews.append({'actor_id': actor_id, 'name' : name, 'profile_path' : profile_path})
#         if len(crews) == 1:
#             break
#     return crews 


# def get_keywords(movie_dict):
#     keywords = []
#     movie_id = movie_dict.get('id')
#     response = requests.get(
#         f'https://api.themoviedb.org/3/movie/{movie_id}/keywords',
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',
#         }
#     ).json()

#     for keyword in response.get('keywords'):
#         keyword_id = keyword.get('id')
#         name=keyword.get('name')
#         keywords.append({'keyword_id' : keyword_id, 'name': name})
#         if len(keywords) == 5:
#             break
#     return keywords
