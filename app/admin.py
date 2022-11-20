from django.contrib import admin
from .models import Producto, Restaurante


admin.site.register(Restaurante)
admin.site.register(Producto)