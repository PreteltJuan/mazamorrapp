from django.shortcuts import render, redirect, HttpResponse
from .models import Cliente, Producto, Restaurante, Usuario, Orden, EstadoOrden, DetalleOrden
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


def loginCliente(request):

    if request.user.is_authenticated:
        try:
            usuario = Cliente.objects.get(username=request.user)
            #usuario2 = Usuario.objects.get(username=request.user)
            return redirect("homeCliente")
        except:
            return redirect("home")
        

    error = False
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    if username and password:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                usuario = Cliente.objects.get(username=request.user)
                userlogin(request, user)
                return redirect("homeCliente")
            except:
                return render(request, "pages/loginCliente.html", {"error": True})
        else:
            error = True

    return render(request, "pages/loginCliente.html", {"error": error})


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



def registroCliente(request):
    error = False
    nombre_campos = [
        "primer_nombre",
        "segundo_nombre",
        "primer_apellido",
        "segundo_apellido",
        "nombre_usuario",
        "correo",
        "clave"
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
        })

        borrar_campos = ("primer_nombre", "primer_apellido",
                         "nombre_usuario", "correo", "clave")

        for campo in borrar_campos:
            campos.pop(campo, None)

        user = Cliente.objects.create_user(**campos)

        if user is not None:
            #userlogin(request, user)
            return HttpResponse("Client account was succesfully created")
        else:
            error = True

    
    return render(request, "pages/registroCliente.html", {"error": error})





def realizar_orden(request):
    if not request.user.is_staff:
        usuario = Usuario.objects.get(username=request.user)
        carritoCompras = Carrito(request)
        for key, value in carritoCompras.carrito.items():
            producto = Producto.objects.get(id=key)
            if producto.unidades < value["cantidad"]:
                return render(request, "pages/compra.html", {'estado': 2})

        for key, value in carritoCompras.carrito.items():
            producto = Producto.objects.get(id=key)
            producto.unidades -= value["cantidad"]

            estadoOrden = EstadoOrden(
                estado = "solicitada"
            )
            estadoOrden.save()

            detallerOrden = DetalleOrden(
                producto = producto,
                precio=producto.precio,
                cantidad=value["cantidad"],
                subTotal=value["acumulado"],
            )
            detallerOrden.save()

            orden = Orden(
                usuario=usuario,
                restaurante = producto.idRestaurante,
                detallerOrden = detallerOrden,
                estadoOrden = estadoOrden,
                )
            orden.save()


            producto.save()

        carritoCompras.limpiar()

        return render(request, "pages/compra.html", {'estado': 1})



def logout(request):
    userlogout(request)
    return redirect("login")



def homeCliente(request):
    if not request.user.is_authenticated:
        return render(request, "pages/loginCliente.html", {"error": False})

    try:
        cliente = Cliente.objects.get(username=request.user)
    except:
        return redirect("home")

    try:
        restaurantes = Restaurante.objects.filter(idCliente = cliente)
    except:
        return HttpResponse("Sin restaurantes")
        return render(request, "pages/homeCliente.html", {"restaurantes": restaurantes, "status":0})

    ordenes = None
    

    data = {
        'lista_restaurantes': restaurantes,
        'restaurantes': len(restaurantes)
    }
    # try:
    #     for i in restaurantes:
    #         ordenes += Orden.objects.filter(restaurante = i)
    # except:
    #     return HttpResponse("Sin ordenes")
    #return redirect("home")
    return render(request, "pages/homeCliente.html", data)
    

def restauranteCliente(request, nombre_r):
    restaurante_b = Restaurante.objects.get(nombre=nombre_r)
    ordenes = Orden.objects.filter(restaurante = restaurante_b)
    cant_items = len(ordenes)
    data = {
        'lista_ordenes': ordenes,
        'ordenes': cant_items
    }
    return render(request, 'pages/restauranteCliente.html', data)


