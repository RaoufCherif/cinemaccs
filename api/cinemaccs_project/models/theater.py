from django.db import models

class Theater(models.Model):
    name = models.CharField(max_length=300)
    zipcode = models.IntegerField()