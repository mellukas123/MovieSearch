from django.urls import path
from . import views
from .views import movie_detail

urlpatterns = [
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]


urlpatterns = [
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
]
