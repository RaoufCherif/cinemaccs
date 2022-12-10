from django.db import models


class RoomPictures(models.Model):
    roomId = models.CharField(max_length=300, null=True)
    picture = models.ImageField( upload_to="pictures/rooms", max_length=255, null=True) 