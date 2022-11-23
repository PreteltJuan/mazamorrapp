from django.contrib import admin
from .models import Cliente, Producto, Restaurante, Usuario, Orden, EstadoOrden, DetalleOrden



admin.site.register(Usuario)
admin.site.register(Restaurante)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(EstadoOrden)
admin.site.register(DetalleOrden)
admin.site.register(Cliente)
