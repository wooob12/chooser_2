from django.contrib import admin
from django.urls import path
from .views import prefer_index, prefer_create, prefer_detail, prefer_delete, prefer_update, prefer_create_comment, prefer_delete_comment


urlpatterns = [
    path('index/', prefer_index, name="prefer_index"),
    path('create/', prefer_create, name="prefer_create"),
    path('detail/<int:prefer_id>', prefer_detail, name="prefer_detail"),
    path('delete/<int:prefer_id>', prefer_delete, name="prefer_delete"),
    path('update/<int:prefer_id>', prefer_update, name="prefer_update"),

    #댓글 기능
    path('prefer_create_comment/<int:prefer_id>/', prefer_create_comment, name="prefer_create_comment"),
    path('prefer_delete_comment/<int:prefer_id>/<int:prefer_comment_id>', prefer_delete_comment, name="prefer_delete_comment"),
]