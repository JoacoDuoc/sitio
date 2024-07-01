from django.contrib import admin
from .models import  Producto, Boleta, Detalle_boleta

# Register your models here.
class admProducto(admin.ModelAdmin):
  list_display=['id','nombre_p','imagen','valor']

admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(Detalle_boleta)