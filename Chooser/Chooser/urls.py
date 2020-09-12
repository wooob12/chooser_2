from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    # 취향소개
    path('prefer/', include('prefer.urls')),
    # 토론                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    # path('debate/', include('debate.urls')),
    
    # 소셜로그인
    path('accounts/', include('allauth.urls')),
]
