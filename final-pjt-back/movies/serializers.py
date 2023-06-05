from rest_framework import serializers
from .models import Movie, Review, Crew, Actor, Genre, LikeReview, Keyword

class CrewSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Crew
        fields = ('id','name','profile_path',)

class ActorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Actor
        fields = ('id','name','profile_path',)

class GenreSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Genre
        fields = ('id','name',)

class ReviewLikeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = LikeReview
        fields = ('id','user.name',)

class ReviewSerializer(serializers.ModelSerializer):
    likeuser = serializers.IntegerField(read_only=True,source='likes.count')
    username = serializers.CharField(read_only=True,source='review_users')
    # likeuser = ReviewLikeSerializer(many=True,read_only=True,source='likes')
    class Meta:
        model = Review
        fields = ('id','content','movie','username','likeuser',)
        read_only_fields = ('movie','review_users')
class KeywordSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Keyword
        fields = ('id','name',)

class MovieSerializer(serializers.ModelSerializer): 
    review = ReviewSerializer(many=True,read_only=True,source='movie_review')
    genre = GenreSerializer(many=True,read_only=True,source='genres')
    actor = ActorSerializer(many=True,read_only=True,source='actors')
    keyword = KeywordSerializer(many=True,read_only=True,source='keywords')
    crew = CrewSerializer(many=True,read_only=True,source='crews')
    likeuser = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Movie
        fields = ('title','id','release_date','keyword','popularity','vote_count','vote_average','overview','poster_path','youtube_key','genre','likeuser','actor','crew','review',)
