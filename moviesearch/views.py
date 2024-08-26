from django.shortcuts import render

import requests
from django.shortcuts import render
from .forms import MovieSearchForm
from django.conf import settings

def search_movie(request):
    form = MovieSearchForm(request.POST or None)
    movie_data = None
    if request.method == 'POST' and form.is_valid():
        title = form.cleaned_data['title']
        api_key = settings.TMDB_API_KEY
        url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}'
        response = requests.get(url)
        movie_data = response.json()
    return render(request, 'moviesearch/search.html', {'form': form, 'movie_data': movie_data})
