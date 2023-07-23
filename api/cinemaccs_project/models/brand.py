from django.db import models


class Brand(models.Model):
    company_name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(
        upload_to="photo/logos", max_length=255, blank=True
    )

    # theater_set
    # theaters
