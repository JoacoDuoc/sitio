from django import forms
from .models import Usuario
from .models import Producto

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['id','nombre_usuario','email','contraseña']

class UpdUsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['id','nombre_usuario','email','contraseña']

#Producto
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['id','nombre_p','imagen','valor']

class UpdProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['id','nombre_p','imagen','valor']