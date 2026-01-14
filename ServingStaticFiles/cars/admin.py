from django.contrib import admin

# Register your models here.

from .models import cars

admin.site.register(cars)
