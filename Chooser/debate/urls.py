from django.contrib import admin
from django.urls import path
from .views import debate_index, debate_create, debate_detail, debate_create_comment, debate_delete_comment


urlpatterns = [
    path('index/', debate_index, name="debate_index"),
    path('create/', debate_create, name="debate_create"),
    path('detail/', debate_detail, name="debate_deatail"),

    #댓글 기능
    path('create_comment/<int:debate_id>/', debate_create_comment, name="debate_create_comment"),
    path('delete_comment/<int:debate_id>/<int:com_pre_id>', debate_delete_comment, name="debate_delete_comment"),
]