from pyexpat import model
from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
