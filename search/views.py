from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return HttpResponse(f"Details for movie: {movie.title}")


from django.shortcuts import render
from .models import Movie

def search_view(request):
    query = request.GET.get('q', '')
    print(f"Search query: {query}")
    if query:
        results = Movie.objects.filter(title__icontains=query)
        print(f"Results: {results}")
    else:
        results = Movie.objects.none()
    return render(request, 'search/search_results.html', {'results': results, 'query': query})

