from django.db import models


class Sessions(models.Model):
    LANGUAGE_CHOICES = [
        ('VO', 'VO'),
        ('VF', 'VF')
    ]
    roomId = models.IntegerField(null=True)
    movieId = models.IntegerField(null=True)
    description = models.CharField(max_length=1000, null=True)
    accessibilityDescription = models.CharField(max_length=1000, null=True)
    sessionTime = models.DateTimeField(null=True)
    language = models.CharField(
        max_length=5,
        choices=LANGUAGE_CHOICES,
        default='VF',        
    )
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    modifiedDate = models.DateTimeField(auto_now=True, null=True)