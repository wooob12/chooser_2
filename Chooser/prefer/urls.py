from django.contrib import admin
from django.urls import path
from .views import prefer_index, prefer_create, prefer_detail, prefer_delete, prefer_update


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index/', prefer_index, name="prefer_index"),
    path('create/', prefer_create, name="prefer_create"),
    path('detail/<int:prefer_id>', prefer_detail, name="prefer_detail"),
    path('delete/<int:prefer_id>', prefer_delete, name="prefer_delete"),
    path('update/<int:prefer_id>', prefer_update, name="prefer_update"),
]