from django.urls import path
from .views import search_movies, movie_detail
from . import views

urlpatterns = [
    path('search/', search_movies, name='search_movie'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('', views.search_movies, name='search_movies'),
]
