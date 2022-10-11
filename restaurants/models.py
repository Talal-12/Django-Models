from pyexpat import model
from django.db import models

# Create your models here.


class Restaurant(models.Model):
    class RestaurantType(models.TextChoices):
        vegan = "vegan"
        Vegetarian = "Vegetarian"
        Keto = "keto"

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=RestaurantType.choices)
    description = models.TextField(DEFAULT="")
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
