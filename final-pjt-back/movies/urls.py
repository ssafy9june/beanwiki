from django.urls import path
from . import views
urlpatterns = [
    # path('tmdb/', views.tmdb_data),
    path('movies/', views.get_movies), #전체 영화 조회
    path('movie/<int:pk>/',views.get_movie_detail), #개별 영화 조회
    path('reviews_like/<int:pk>/',views.review_like), #리뷰 좋아요
    path('movie_like/<int:movieid>/', views.movie_like), # 영화 좋아요
    path('find_movies/title/<str:search>/', views.find_movies_title), #영화 검색 - 제목
    path('find_movies/actor/<str:search>/', views.find_movies_actor), #영화 검색 - 배우
    path('find_movies/crew/<str:search>/', views.find_movies_crew), #영화 검색 - 감독
    path('find_movies/genre/<str:search>/', views.find_movies_genre), #영화 검색 - 장르
    path('search_actor/<str:search>/', views.search_actor), #배우 검색
    path('search_crew/<str:search>/', views.search_crew), #감독 검색
    path('like_movies/<int:userid>/', views.like_movies), # 좋아요 누른 영화

    # 클릭

    path('click/<int:userid>/', views.click), #영화 검색 - 장르

    # 리뷰 작성
    path('review_create/<int:movieid>/', views.review_create),
    path('review_like/<int:reviewid>/', views.review_like),
    
    
    # 영화 추천 알고리즘 


    path('recommend_main/<int:userid>/', views.recommend_main), # 전체 추천
    path('recommend_actor/<int:userid>/', views.recommend_actors), # 배우 추천
    path('recommend_genre/<int:userid>/', views.recommend_genres), # 장르 추천
    path('recommend_crew/<int:userid>/', views.recommend_crews), # 감독 추천
    path('recommend_trend/', views.recommend_trend), # 트렌드 추천
    path('recommend_movie/<int:movieid>/', views.recommend_movie), # 특정 영화 관련 추천
    path('more_movies/<str:type>/<str:keyword>/', views.all_movies), # 더보기 기능

    # bard
    
    path('find_movie_by_bard/', views.find_movie_by_bard), # 영화 검색




    # path('create_csv/',views.export_movies_csv), # 추천 알고리즘 csv 생성
    # path('click_csv/<int:user_id>/', views.click_csv),
    # path('recommend_keywords/<str:search>/', views.recommend_keywords), #영화 추천
    # path('recommend_genres/<str:search>/', views.recommend_genres), #장르 기반
    # path('recommend_actors/<str:search>/', views.recommend_actors), #배우 기반
    # path('test/', views.make_recommend),

]
