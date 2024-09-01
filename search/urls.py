from django.urls import path
from .views import search_view  # Import the views module from the current directory

urlpatterns = [
    path('', search_view, name='search'),  # Define URL patterns
]
