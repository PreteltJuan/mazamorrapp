
from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    time = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre

class OrderStatus(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    date = models.DateTimeField()
    def __str__(self):
        return str(self.order)


class Restaurante(models.Model):
    idRestaurante = models.AutoField(primary_key=True, null=False), 
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

        