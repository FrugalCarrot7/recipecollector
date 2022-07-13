from django.contrib import admin
from .models import Recipe, Step

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Step)