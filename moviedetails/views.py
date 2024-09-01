# from django.shortcuts import render
# import requests
# from django.conf import settings
#
#
# def movie_detail(request, movie_id):
#     """
#     Vaade, mis kuvab valitud filmi üksikasjaliku teabe.
#     """
#     api_key = settings.TMDB_API_KEY
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=credits'
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         movie = response.json()
#         return render(request, 'moviedetails/movie_detail.html', {'movie': movie})
#     else:
#         return render(request, 'moviedetails/error.html', {'message': 'Movie not found'})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, MovieBookmark
import requests
from django.conf import settings

@login_required
def movie_detail(request, movie_id):
    api_key = settings.TMDB_API_KEY
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=credits'
    response = requests.get(url)
    movie = response.json()

    # Check if the movie is bookmarked
    is_bookmarked = MovieBookmark.objects.filter(user=request.user, movie__id=movie_id).exists()

    if request.method == 'POST':
        if 'bookmark' in request.POST:
            # Handle the bookmarking
            if not is_bookmarked:
                movie_instance, created = Movie.objects.get_or_create(
                    title=movie['title'],
                    defaults={
                        'release_date': movie['release_date'],
                        'poster_path': movie['poster_path'],
                        'overview': movie['overview'],
                        'genres': movie['genres']
                    }
                )
                MovieBookmark.objects.create(user=request.user, movie=movie_instance)
        elif 'remove_bookmark' in request.POST:
            # Handle the removing of the bookmark
            if is_bookmarked:
                MovieBookmark.objects.filter(user=request.user, movie__id=movie_id).delete()
        return redirect('movie_detail', movie_id=movie_id)

    return render(request, 'moviedetails/movie_detail.html', {
        'movie': movie,
        'is_bookmarked': is_bookmarked
    })
