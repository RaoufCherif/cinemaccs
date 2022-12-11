from django.db import models
from cinemaccs_project.models.room import Room


class RoomPicture(models.Model):
    room_id = models.ForeignKey(Room, related_name='pictures', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/rooms", max_length=255, null=True)
