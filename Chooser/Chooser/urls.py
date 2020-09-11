from django.contrib import admin
from django.urls import include,path
# Media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),

    # 취향소개
    path('prefer/', include('prefer.urls')),

    # 토론
    path('debate/', include('debate.urls')),
    
    # 소셜로그인
    path('accounts/', include('allauth.urls')),

    # MEDIA 추가
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
