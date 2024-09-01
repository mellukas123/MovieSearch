# from django.db import models
#
# print("Loading search/models.py")
#
# class Movie(models.Model):
#     title = models.CharField(max_length=255)
#     release_date = models.DateField()
#
#     def __str__(self):
#         return self.title

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()  # This line should be present
    release_date = models.DateField()
