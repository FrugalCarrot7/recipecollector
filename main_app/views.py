from django.shortcuts import render
from django.http import HttpResponse

#temp data
class Recipe:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, ingredients, description):
    self.name = name
    self.ingredients = ingredients
    self.description = description

recipes = [
  Recipe('Pizza', 'Bread, Cheese, Tomato Sauce', 'tasty goodness'),
  Recipe('Blueberry Pie', 'pie', 'A pie made with blueberries'),
  Recipe('a food', 'its ingredients', 'its description')
]

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
  return render(request, 'recipes/index.html', { 'recipes': recipes })

  #update Recipe class above!!