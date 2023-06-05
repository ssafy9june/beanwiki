from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles), # 전체글 조회
    path('article/<int:userid>/', views.article), # 글 삭제, 생성
    path('comment/<int:userid>/', views.comment), #댓글 작성
    path('like_article/<int:userid>/', views.like_article), # 글 좋아요
]
