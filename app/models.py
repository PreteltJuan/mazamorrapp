
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



        