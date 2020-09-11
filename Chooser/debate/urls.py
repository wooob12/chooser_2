from django.contrib import admin
from django.urls import path
from .views import debate_index, debate_create, debate_detail


urlpatterns = [
    path('index/', debate_index, name="debate_index"),
    path('create/', debate_create, name="debate_create"),
    path('detail/', debate_detail, name="debate_deatail"),
]