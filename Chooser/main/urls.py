from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('login/', views.signin, name = 'login'),
    path('logout/', views.signout, name = 'logout'),
    path('join/',views.join, name = 'join'),
    path('mypage/', views.mypage, name = 'mypage'), 

    #소셜로그인 관련
    path('accounts/', include('allauth.urls')),
]