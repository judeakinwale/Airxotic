from django.db import models

# Create your models here.


class Air(models.Model):
    location = models.CharField(max_length=120)
    description = models.TextField(max_length=250, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    sale_price = models.DecimalField(max_digits=7, decimal_places=2)


class AirImage(models.Model):
    air = models.ManyToManyField(Air)
    image = models.ImageField(blank=True)
    pass