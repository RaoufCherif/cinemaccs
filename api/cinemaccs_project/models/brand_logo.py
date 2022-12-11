from django.db import models


class BrandLogo(models.Model):
    brand = models.CharField(max_length=300, null=True)
    logo = models.ImageField(
        upload_to="pictures/logo", max_length=255, null=True
    )
