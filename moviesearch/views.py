from django.shortcuts import render, get_object_or_404
import requests
from django.conf import settings
from .forms import MovieSearchForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import MovieBookmark
from .forms import BookmarkForm
import requests
from django.conf import settings



def search_movies(request):
    """
    Handle movie search by title and display results.
    """
    form = MovieSearchForm(request.POST or None)
    movies = []

    if request.method == 'POST' and form.is_valid():
        title = form.cleaned_data['title']
        api_key = settings.TMDB_API_KEY
        url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}'
        response = requests.get(url)
        movies = response.json().get('results', [])

    return render(request, 'moviesearch/search.html', {'form': form, 'movies': movies})


@login_required
def movie_detail(request, movie_id):
    api_key = settings.TMDB_API_KEY
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=credits'
    response = requests.get(url)
    movie = response.json()

    # Check if the movie is bookmarked
    is_bookmarked = MovieBookmark.objects.filter(user=request.user, movie_id=movie_id).exists()

    if request.method == 'POST':
        if 'bookmark' in request.POST:
            # Handle the bookmarking
            if not is_bookmarked:
                MovieBookmark.objects.create(user=request.user, movie_id=movie_id)
        elif 'remove_bookmark' in request.POST:
            # Handle the removing of the bookmark
            if is_bookmarked:
                MovieBookmark.objects.filter(user=request.user, movie_id=movie_id).delete()
        return redirect('movie_detail', movie_id=movie_id)

    return render(request, 'moviedetails/movie_detail.html', {
        'movie': movie,
        'is_bookmarked': is_bookmarked
    })