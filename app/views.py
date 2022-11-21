from django.shortcuts import render, redirect
from .models import  Producto, Restaurante, Usuario, Orden, EstadoOrden, DetalleOrden
from .carrito import Carrito
from django.contrib.auth import authenticate, login as userlogin, logout as userlogout, get_user_model

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
    



def agregar_producto_carrito(request, producto_id):
    carritoCompras = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carritoCompras.agregar(producto)
    return redirect(request.META.get('HTTP_REFERER'))


def eliminar_producto_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.eliminar(producto)
    return redirect(request.META.get('HTTP_REFERER'))


def eliminar_unidad_producto_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.eliminarUnidad(producto)
    return redirect(request.META.get('HTTP_REFERER'))


def limpiar_carrito(request):
    carritoCompras = Carrito(request)
    carritoCompras.limpiar()
    return redirect(request.META.get('HTTP_REFERER'))


def compra(request):
    usuario = Usuario.objects.get(username=request.user)

    data = {
        'usuario': usuario,
    }
    return render(request, "pages/compra.html", data)

def login(request):

    if request.user.is_authenticated:
        return redirect("home")

    error = False
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    if username and password:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            userlogin(request, user)
            return redirect("home")
        else:
            error = True

    return render(request, "pages/login.html", {"error": error})


def registro(request):
    error = False
    nombre_campos = [
        "primer_nombre",
        "segundo_nombre",
        "primer_apellido",
        "segundo_apellido",
        "nombre_usuario",
        "correo",
        "clave",
        "barrio",
        "direccion",
        "fecha",
        "sexo",
    ]

    campos = {
        nombre: request.POST.get(nombre, "")
        for nombre in nombre_campos
    }

    crear_usuario = campos.get("nombre_usuario")
    if crear_usuario:
        campos.update({
            "first_name": campos.get("primer_nombre"),
            "last_name": campos.get("primer_apellido"),
            "username": campos.get("nombre_usuario"),
            "email": campos.get("correo"),
            "password": campos.get("clave"),
            "fecha_nacimiento": campos.get("fecha")
        })

        borrar_campos = ("primer_nombre", "primer_apellido",
                         "nombre_usuario", "correo", "clave", "fecha")

        for campo in borrar_campos:
            campos.pop(campo, None)

        user = Usuario.objects.create_user(**campos)

        if user is not None:
            userlogin(request, user)
            return redirect("home")
        else:
            error = True

    return render(request, "pages/registro.html", {"error": error})



def realizar_orden(request):
    if not request.user.is_staff:
        usuario = Usuario.objects.get(username=request.user)
        carritoCompras = Carrito(request)
        for key, value in carritoCompras.carrito.items():
            producto = Producto.objects.get(id=key)
            if producto.unidades < value["cantidad"]:
                return render(request, "pages/compra.html", {'estado': 2})

        orden = Orden(
            usuario=usuario,
            precio=carritoCompras.subTotal)
        orden.save()

        estadoOrden = EstadoOrden(
            orden = orden,
            estado = "solicitada"
        )
        estadoOrden.save()

        for key, value in carritoCompras.carrito.items():
            producto = Producto.objects.get(id=key)
            producto.unidades -= value["cantidad"]
            detallerOrden = DetalleOrden(
                orden = orden,
                producto = producto,
                precio=producto.precio,
                cantidad=value["cantidad"],
                subTotal=value["acumulado"],
            )
            detallerOrden.save()
            producto.save()

        carritoCompras.limpiar()

        return render(request, "pages/compra.html", {'estado': 1})
