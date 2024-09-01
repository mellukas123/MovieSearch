from django.db import models
from django.contrib.auth.models import User  # Import User model
from moviedetails.models import Movie  # Import Movie model from moviedetails app

class MovieBookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moviesearch_bookmarks')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moviesearch_bookmarked_by')
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')  # Ensures a user can only bookmark a movie once

    def __str__(self):
        return f"{self.user.username} bookmarked {self.movie.title}"
