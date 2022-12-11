from django.db import models


class Session(models.Model):
    LANGUAGE_CHOICES = [
        ('VO', 'VO'),
        ('VF', 'VF')
    ]
    room_id = models.IntegerField(null=True)
    movie_id = models.IntegerField(null=True)
    internal_session_id = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=1000, null=True)
    accessibility_description = models.CharField(max_length=1000, null=True)
    session_time = models.DateTimeField(null=True)
    language = models.CharField(
        max_length=5,
        choices=LANGUAGE_CHOICES,
        default='VF',
    )
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
