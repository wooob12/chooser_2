from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),

    #소셜로그인 관련
    path('accounts/', include('allauth.urls')),
]