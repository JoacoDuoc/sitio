from django.contrib import admin
from .models import  Producto

# Register your models here.
class admProducto(admin.ModelAdmin):
  list_display=['id','nombre_p','imagen','valor']

admin.site.register(Producto)