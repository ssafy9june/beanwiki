from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.TextField(null=True)
    popularity = models.FloatField(null=True)

class Crew(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    
class Keyword(models.Model):
    name = models.TextField(null=True)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200,null=True)
    youtube_key = models.CharField(max_length=100,null=True)
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_movies')
    actors = models.ManyToManyField(Actor)
    crews = models.ManyToManyField(Crew)
    keywords = models.ManyToManyField(Keyword)

class Click(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    userid = models.IntegerField()

class Review(models.Model):
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_review')
    review_users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_likes')
    

class LikeReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')

class RecommendKeyword(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movieid = models.TextField()
    origin = models.TextField()
    movie_title = models.TextField()
    score = models.FloatField()

class RecommendGenres(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movieid = models.TextField()
    origin = models.TextField()
    movie_title = models.TextField()
    score = models.FloatField()

class RecommendActors(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movieid = models.TextField()
    origin = models.TextField()
    movie_title = models.TextField()
    score = models.FloatField()