from django.urls import path
from . import views

urlpatterns = [
    path('', views.userid), # 유저 아이디 받아오기
    path('profile/<int:userid>/', views.profile), # 프로필 조회
    path('reset_algorithm/<int:userid>/', views.reset_algorithm), # 알고리즘 초기화
    path('following/<int:userid>/', views.followings),
    
]
