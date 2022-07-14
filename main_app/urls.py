from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('recipes/', views.recipes_index, name='index'),
  path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
  path('recipes/create', views.RecipeCreate.as_view(), name="recipes_create"),
  path('recipes/<int:pk>/update', views.RecipeUpdate.as_view(), name="recipes_update"),
  path('recipes/<int:pk>/delete', views.RecipeDelete.as_view(), name="recipes_delete"),
  path('recipes/<int:recipe_id>/add_step/', views.add_step, name='add_step'),
  path('sides/', views.SideList.as_view(), name='sides_index'),
  path('sides/<int:pk>/', views.SideDetail.as_view(), name='sides_detail'),
  path('sides/create/', views.SideCreate.as_view(), name='sides_create'),
  path('sides/<int:pk>/update/', views.SideUpdate.as_view(), name='sides_update'),
  path('sides/<int:pk>/delete/', views.SideDelete.as_view(), name='sides_delete'),
  path('recipes/<int:recipe_id>/assoc_side/<int:side_id>/', views.assoc_side, name='assoc_side'),
]

