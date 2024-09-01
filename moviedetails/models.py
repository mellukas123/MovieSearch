from django.db import models
from django.conf import settings

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    genres = models.JSONField(blank=True, null=True)  # Assuming genres are stored in JSON format

    def __str__(self):
        return self.title

class MovieBookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moviedetails_bookmarked_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')
        verbose_name = 'Movie Bookmark'
        verbose_name_plural = 'Movie Bookmarks'

    def __str__(self):
        return f'{self.user.username} bookmarked movie {self.movie.title}'
