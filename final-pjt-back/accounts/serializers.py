from rest_framework import serializers
from .models import User
from movies.models import Movie, Click
from movies.serializers import MovieSerializer 
# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('id', 'title', 'release_date', 'popularity', 'vote_count', 'vote_average', 'overview', 'poster_path', 'youtube_key','like_users',)
class ClickSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(read_only=True,source='movie')
    class Meta:
        model = Click
        fields = '__all__'
        read_only_fields = ('movies',)
        
        
class UserSerializer(serializers.ModelSerializer):
    likemovies = MovieSerializer(read_only=True, many=True, source='liked_movies')
    # class SimpleUserSerializer(serializers.ModelSerializer):
    #     follwowers = M
    class Meta:
        model = User
        fields = ('followings','likemovies', 'followers', 'username')
        read_only_fields = ('likemovies',)
