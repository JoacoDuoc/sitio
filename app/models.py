from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Usuario(models.Model):
    id=models.IntegerField( primary_key=True , null=False)
    nombre_usuario=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=50,null=False)
    contraseña= models.CharField(max_length=50,null=False)

class Producto(models.Model):
    id=models.IntegerField( primary_key=True , null=False)
    nombre_p = models.CharField( max_length=50,null=False)
    # imagen
    valor = models.IntegerField(null=False)

class Pedidos(models.Model):
    id_pedido = models.IntegerField( primary_key=True , null=False)
    cliente = models.CharField(max_length=50 , null=False)
    email = models.CharField(max_length=50, null=50)
    valor = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1000000)] ,null=False)
    detalle = models.CharField(max_length=50, null=False)

class Carrito(models.Model):
    #imagen
    detalle_p = models.CharField(max_length=50, null=False)
    valor = models.IntegerField(null=False)

class Perfil(models.Model):
    nombre_u = models.CharField(max_length=50, null=False)
    gmail = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    #foto

class Deseados(models.Model):
    #imagen
    detalle_p = models.CharField(max_length=50, null=False)
    valor = models.IntegerField(null=False)

class Historial_c(models.Model):
    # imagen
    descripcion = models.CharField(max_length=50, null=False)

