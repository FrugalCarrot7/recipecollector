from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Recipe, Side
from .forms import StepForm

#temp data


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', { 'recipes': recipes })

def recipes_detail(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  step_form = StepForm()
  return render(request, 'recipes/detail.html', { 'recipe': recipe, 'step_form': step_form })

class RecipeCreate(CreateView):
  model = Recipe
  fields = '__all__'
  # success_url = '/cats/'

class RecipeUpdate(UpdateView):
  model = Recipe
  fields = '__all__'

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes/'

def add_step(request, recipe_id):
  form = StepForm(request.POST)
  if form.is_valid():
    new_step = form.save(commit=False)
    new_step.recipe_id = recipe_id 
    new_step.save()
  return redirect('detail', recipe_id=recipe_id)

class SideList(ListView):
  model = Side

class SideDetail(DetailView):
  model = Side

class SideCreate(CreateView):
  model = Side
  fields = '__all__'
  success_url = '/recipes/'

class SideUpdate(UpdateView):
  model = Side
  fields = ['name', 'price']

class SideDelete(DeleteView):
  model = Side
  success_url = '/recipes/'