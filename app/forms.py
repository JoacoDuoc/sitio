from django import forms
from .models import  Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Producto
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'

class UpdProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['id','nombre_p', 'valor']

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name" , "last_name", "email", "password1" ,"password2"]