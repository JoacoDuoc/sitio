from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Usuario(models.Model):
    id=models.IntegerField( primary_key=True , null=False)
    nombre_usuario=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=50,null=False)
    contraseña= models.CharField(max_length=50,null=False)

    def __str__(self):
        return f"Id: {self.id} Nombre: {self.nombre_usuario}"

class Producto(models.Model):
    id=models.IntegerField( primary_key=True , null=False)
    nombre_p = models.CharField( max_length=50,null=False)
    imagen = models.ImageField("Imagen", upload_to='add_producto', null=True)
    valor = models.IntegerField(null=False)

    def __str__(self):
        return self.nombre_p
    

class Pedidos(models.Model):
    id_pedido = models.IntegerField( primary_key=True , null=False)
    cliente = models.ForeignKey(Usuario , on_delete=models.PROTECT)
    email = models.CharField(max_length=50, null=50)
    valor = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1000000)] ,null=False)
    detalle = models.CharField(max_length=50, null=False)

class Carrito(models.Model):
    videojuego = models.ForeignKey(Producto , on_delete=models.PROTECT)
    valor = models.IntegerField(null=False)

class Perfil(models.Model):
    nombre_u = models.CharField(max_length=50, null=False)
    gmail = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    foto_perfil = models.ImageField("Imagen", upload_to='editar_perfil')

class Deseados(models.Model):
    videojego_deseado = models.ForeignKey(Producto , on_delete=models.PROTECT)

class Historial_c(models.Model):
    videojuego_comprado = models.ForeignKey(Producto , on_delete=models.PROTECT)

