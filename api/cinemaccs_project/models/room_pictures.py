from django.db import models


class RoomPicture(models.Model):
    roomId = models.ForeignKey(Room, related_name='pictures', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="pictures/rooms", max_length=255, null=True)
