from django.urls import path
from . import views


urlpatterns = [
    path("home", views.clientesHome,  name="home"),
    path("restaurante/<nombre_r>", views.restaurante,  name="restaurante"),
    path('agregarCarrito/<int:producto_id>/', views.agregar_producto_carrito, name="agregarAlCarrito"),
    path('eliminarCarrito/<int:producto_id>/', views.eliminar_producto_carrito, name="eliminarCarrito"),
    path('eliminarUnidadCarrito/<int:producto_id>/', views.eliminar_unidad_producto_carrito, name="eliminarUnidadCarrito"),
    path('limpiar', views.limpiar_carrito, name="limpiar"),
]