from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=300, null=True)
    duration = models.CharField(max_length=300, null=True)
    allocine_id = models.CharField(max_length=10, null=True)
    isan_id = models.CharField(max_length=50, null=True)
    poster = models.ImageField(upload_to="photos/movies", max_length=255, null=True)
    release_date = models.DateTimeField(null=True)
    synopsis = models.CharField(max_length=500, null=True)
    director = models.CharField(max_length=300, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
