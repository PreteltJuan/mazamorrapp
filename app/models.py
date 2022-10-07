from email.headerregistry import Address
from django.db import models

# Create your models here.

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    comuna = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class Peticiones(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    time = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre