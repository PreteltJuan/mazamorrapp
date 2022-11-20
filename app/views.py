from django.shortcuts import render, redirect
from .forms import OrderRequest
from .models import Order, Producto, Restaurante

def clientesHome(request):
    restaurantes = Restaurante.objects.all()
    cant_items = len(restaurantes)
    data = {
        'lista_restaurantes': restaurantes,
        'items': cant_items
    }
    return render(request, 'pages/home.html', data)

def restaurante(request, nombre_r):
    restaurante_b = Restaurante.objects.get(nombre=nombre_r)
    productos = Producto.objects.filter(idRestaurante = restaurante_b)
    cant_items = len(productos)
    data = {
        'lista_productos': productos,
        'items': cant_items
    }
    return render(request, 'pages/restaurante.html', data)


def restauranteProducto(request, nombre_r, producto_id):
    restaurante_b = Restaurante.objects.get(nombre=nombre_r)
    productos = Producto.objects.filter(idRestaurante = restaurante_b)
    producto = Producto.objects.get(id = producto_id)
    cant_items = len(productos)
    data = {
        'lista_productos': productos,
        'items': cant_items,
        'producto': producto
    }
    return render(request, 'pages/restaurante.html', data)
    
def vendedoresHome(request):
    orders = Order.objects.all()
    return render(request, 'pages/vendedorHome.html', { 'orders' : orders})
    






    