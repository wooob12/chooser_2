from django.urls import path
from .views import debate_index, debate_create, debate_detail


urlpatterns = [
    path('debate_index/', debate_index, name="debate_index"),
    path('debate_create/', debate_create, name="debate_create"),
    path('debate_detail/', debate_detail, name="debate_deatail"),
]