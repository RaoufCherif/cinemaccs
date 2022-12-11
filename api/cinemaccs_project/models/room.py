from django.db import models


class Room(models.Model):
    ACCESS_CHOICES = [
        ('bottom', 'bottom'),
        ('middle', 'middle'),
        ('top', 'top'),
    ]
    internal_room_id = models.CharField(max_length=20, null=True)
    seats = models.IntegerField(null=True)
    access_point = models.CharField(
        max_length=10,
        choices=ACCESS_CHOICES,
        null=True,
    )
    wheelchair_spaces = models.IntegerField(null=True)
    description = models.CharField(max_length=1000, null=True)
    accessibility_description = models.CharField(max_length=1000, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    # pictures
