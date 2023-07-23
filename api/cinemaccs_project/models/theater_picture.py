from django.db import models

from cinemaccs_project.models import Theater


class TheaterPicture(models.Model):
    theater = models.ForeignKey(
        Theater, related_name="pictures", on_delete=models.CASCADE
    )
    legend = models.CharField(max_length=1000, null=True)
    photo = models.ImageField(
        upload_to="photos/theaters", max_length=255, null=True
    )
