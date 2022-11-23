from django.urls import path
from . import views


urlpatterns = [
    path("home", views.clientesHome,  name="home"),
    path("restaurante/<nombre_r>", views.restaurante,  name="restaurante"),
    path('agregarCarrito/<int:producto_id>/', views.agregar_producto_carrito, name="agregarAlCarrito"),
    path('eliminarCarrito/<int:producto_id>/', views.eliminar_producto_carrito, name="eliminarCarrito"),
    path('eliminarUnidadCarrito/<int:producto_id>/', views.eliminar_unidad_producto_carrito, name="eliminarUnidadCarrito"),
    path('limpiar', views.limpiar_carrito, name="limpiar"),
    path("compra", views.compra, name="compra"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("registro", views.registro, name="registro"),
    path('realizarOrden', views.realizar_orden, name="realizarOrden"),
    path('registroCliente', views.registroCliente, name="registroCliente"),
    path("loginCliente", views.loginCliente, name="loginCliente"),
    path("homeCliente", views.homeCliente, name="homeCliente"),
    path("restauranteCliente/<nombre_r>", views.restauranteCliente,  name="restauranteCliente"),
    #path("cambiarEstado/<id>", views.cambiarEstado, name="cambiarEstado") <-- falta eso
]