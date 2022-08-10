from atexit import register
from django.contrib import admin
from .models import Lumpia, Dessert

# Register your models here.

admin.site.register(Lumpia)
admin.site.register(Dessert)
