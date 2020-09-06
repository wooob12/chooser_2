from django.contrib import admin
from django.urls import path
from .views import prefer_index, prefer_create, prefer_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefer_index/', prefer_index, name="prefer_index"),
    path('prefer_create/', prefer_create, name="prefer_create"),
    path('prefer_detail/', prefer_detail, name="prefer_detail"),
]