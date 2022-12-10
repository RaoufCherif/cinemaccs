from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=300, null=True)
    duration = models.CharField(max_length=300, null=True)
    allocineId = models.CharField(max_length=10, null=True)
    isanId = models.CharField(max_length=50, null=True)
    poster = models.ImageField(upload_to="pictures/movies", max_length=255, null=True) 
    releaseDate = models.DateTimeField(null=True)
    synopsis = models.CharField(max_length=500, null=True)
    director = models.CharField(max_length=300, null=True)
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    modifiedDate = models.DateTimeField(auto_now=True, null=True)