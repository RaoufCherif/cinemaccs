from django.db import models

from cinemaccs_project.models import Theater, DescriptionElement


class Room(models.Model):

    ACCESS_CHOICES = [
        ("bottom", "bottom"),
        ("middle", "middle"),
        ("top", "top"),
    ]

    theater = models.ForeignKey(
        Theater, related_name='theaters', null=True, on_delete=models.CASCADE
    )

    internal_room_id = models.CharField(max_length=20, null=True)
    seats = models.IntegerField(null=True)
    access_point = models.CharField(
        max_length=10,
        choices=ACCESS_CHOICES,
        null=True,
    )
    wheelchair_spaces = models.IntegerField(null=True)

    description = models.CharField(max_length=1000, null=True)
    description_elements = models.ManyToManyField(
        DescriptionElement, blank=True
    )

    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    # room_picture_set
    # pictures

    @property
    def description_elements_kwargs(self):
        # Suppose a prefetch
        return {
            e.id: e.text for e in self.description_elements
        }

    @property
    def accessibility_description(self):
        return (
            self.description + '\n'
            + ' '.join([v for _, v in self.description_elements_kwargs])
        )
