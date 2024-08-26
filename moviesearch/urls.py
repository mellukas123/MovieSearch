from django.urls import path
from .views import search_movie

urlpatterns = [
    path('search/', search_movie, name='search_movie'),
]
