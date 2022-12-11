from django.db import models


class BrandLogo(models.Model):
    brand = models.CharField(max_length=300, null=True)
    photo = models.ImageField(
        upload_to="photo/logos", max_length=255, null=True
    )
