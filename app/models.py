from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import uuid


# Create your models here.

class Producto(models.Model):
    id=models.IntegerField( primary_key=True ,default=uuid.uuid4, null=False)
    nombre_p = models.CharField( max_length=50,null=False)
    imagen = models.ImageField("Imagen", upload_to='add_producto', null=True)
    valor = models.IntegerField(null=False)

    def __str__(self):
        return self.nombre_p

class Boleta (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fechaVenta = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(User,on_delete=models.CASCADE)
    completada = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)
    @property
    def get_total(self):
        detalle = self.detalle_boleta_set.all()
        total = sum([item.producto.valor * item.cantidad_productos for item in detalle])
        return total
    @property
    def get_item(self):
        detalle = self.detalle_boleta_set.all()
        total = sum([item.cantidad_productos for item in detalle])
        return total
    
class Detalle_boleta (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    cantidad_productos = models.IntegerField(default=0) 
    def __str__(self):
        return str(self.boleta.id) + '-' + self.producto.nombre_p
    @property
    def get_total(self):
        total = self.producto.valor * self.cantidad_productos
        return total
    
class Perfil(models.Model):
    nombre_u = models.CharField(max_length=50, null=False)
    gmail = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    foto_perfil = models.ImageField("Imagen", upload_to='editar_perfil')

class Deseados(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.PROTECT)
    usuario = models.CharField(max_length=50, null= False)
    
    def __str__(self):
        return f'Lista de deseados de {self.usuario} - Producto: {self.producto.nombre_p}'

class Historial_c(models.Model):
    usuario = models.CharField(max_length=50, null=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Compra de {self.producto.nombre_p} por {self.usuario}'
