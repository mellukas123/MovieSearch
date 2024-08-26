from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

API_KEY = '50cffaaf30c01354972ef7e5f8870e81'

def search_movies(request):
    query = request.GET.get('query', '')
    movies = []
    if query:
        response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}')
        data = response.json()
        movies = data.get('results', [])
    return render(request, 'moviesearch/search.html', {'movies': movies})
