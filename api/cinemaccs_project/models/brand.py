from django.db import models


class Brand(models.Model):
    company_name = models.CharField(max_length=300)
    logo = models.ImageField(upload_to="photo/logos", max_length=255)
