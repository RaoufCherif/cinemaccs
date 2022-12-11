from django.db import models


class TheaterPicture(models.Model):
    theater_id = models.CharField(max_length=300, null=True)
    picture = models.ImageField(upload_to="pictures/theaters", max_length=255, null=True) 