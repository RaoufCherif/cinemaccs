from django.db import models


class Room(models.Model):
    ACCESS_CHOICES = [
        ('bottom', 'bottom'),
        ('middle', 'middle'),
        ('top', 'top'),
    ]
    internalRoomId = models.CharField(max_length=20, null=True)
    seats = models.IntegerField(null=True)
    accessPoint = models.CharField(
        max_length=10,
        choices=ACCESS_CHOICES,
        null=True,        
    )
    wheelchairSpaces = models.IntegerField(null=True)
    description = models.CharField(max_length=1000, null=True)
    accessibilityDescription = models.CharField(max_length=1000, null=True)
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    modifiedDate = models.DateTimeField(auto_now=True, null=True)