from django.db import models
from django.urls import reverse

# Create your models here.
class Side(models.Model):
  name = models.CharField(max_length=20)
  price = models.IntegerField()

  def get_absolute_url(self):
    return reverse('ingredients_detail', kwargs={'pk': self.id})

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    sides = models.ManyToManyField(Side)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})

class Step(models.Model):
  step = models.IntegerField('add the step number')
  instructions = models.CharField(max_length=500)

  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)