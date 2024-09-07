from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Movie
import requests
from movieproject.settings import TMDB_API_KEY


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return HttpResponse(f"Details for movie: {movie.title}")


def search_view(request):
    query = request.GET.get('q', '')
    print(f"Search query: {query}")
    if query:
        request_body = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page=1"
        headers = {

            "accept": "application/json",
            "Authorization": f"Bearer {'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MGNmZmFhZjMwYzAxMzU0OTcyZWY3ZTVmODg3MGU4MSIsIm5iZiI6MTcyNTE4MDA2MC4xNzExODgsInN1YiI6IjY2Y2E0MTU1NzZmODQwY2JmNmRhOTcyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jH4hzAp6R2JIbjR_DppyrKs7VSidnCvVCISm6ZLSEeo'}"
        }
        results = requests.get(request_body, headers=headers)
        results = results.json()
        print(f"Results: {results}")
    else:
        results =  {"results" : Movie.objects.none()}
    results
    return render(request, 'search/search_results.html', {'results': results['results'], 'query': query})

