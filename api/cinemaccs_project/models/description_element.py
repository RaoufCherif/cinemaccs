from django.db import models


class DescriptionElement(models.Model):
    PMR = 'PMR'
    HANDICAP_FAMILLY_CHOICES = [
        (PMR, 'Mobility'),
    ]
    handicap_familly = models.CharField(
        max_length=5,
        choices=HANDICAP_FAMILLY_CHOICES,
        default=PMR,
    )
    text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
