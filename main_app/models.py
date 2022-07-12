from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=50)
    description = models.CharField(max_length=500)