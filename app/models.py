
from django.db import models
from django.contrib.auth.models import User


class Usuario(User):
    segundo_nombre = models.CharField(max_length=40, null=True)
    segundo_apellido = models.CharField(max_length=40, null=True)
    direccion = models.CharField(max_length=128)
    barrio = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=16)

    def __str__(self):
        return self.primer_nombre

    @property
    def primer_nombre(self):
        return self.first_name

class Cliente(User):
    segundo_nombre = models.CharField(max_length=40, null=True)
    segundo_apellido = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.primer_nombre

    @property
    def primer_nombre(self):
        return self.first_name

class Restaurante(models.Model):
    idRestaurante = models.AutoField(primary_key=True, null=False),
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=50, unique=True)
    imagen = models.ImageField(upload_to="productos", null=False)
    logo = models.ImageField(upload_to="productos", null=True)
    popularidad = models.IntegerField(default=0)
    estrellas = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre



class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, null=False), 
    idRestaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precioAnterior = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    unidades = models.IntegerField(default=0)
    nuevo = models.BooleanField(default=False, null=False)
    descuento = models.BooleanField(default=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to="productos", null=False)
    popularidad = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre






class EstadoOrden(models.Model):
    estado = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.estado)

class DetalleOrden(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    subTotal = models.IntegerField(default=0)
    def __str__(self):
        return  str(self.producto)

class Orden(models.Model):
    idOrden = models.AutoField(primary_key=True, null=False),
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    detallerOrden = models.ForeignKey(DetalleOrden, on_delete=models.CASCADE)
    estadoOrden = models.ForeignKey(EstadoOrden, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.idOrden)