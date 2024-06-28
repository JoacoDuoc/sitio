from django.shortcuts import render,  redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm,CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import logout
from django.contrib.auth import authenticate , login

# Create your views here.\
def salir(request):
    logout(request)
    messages.info(request,'Sesion Cerrada')
    return redirect(to="index")


def index(request):
    productos = Producto.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data={
        'productos': productos
    }
    return render(request, 'app/index.html', data)

def recuperar_pswd(request):
    return render(request, 'app/recuperar_pswd.html')

def email_recuperar_pswd(request):
    return render(request, 'app/email_recuperar_pswd.html')

def detalle_game(request, id):
    producto=get_object_or_404(Producto,id=id)
    datos = {

        "producto":producto
    }
    return render(request, 'app/detalle_game.html', datos)

def carrito(request):
    return render(request, 'app/carrito.html')

def pago(request):
    return render(request, 'app/pago.html')

def finpago(request):
    return render(request, 'app/finpago.html')

def filtro(request):
    return render(request, 'app/filtro.html')

def favs(request):
    return render(request, 'app/favs.html')

def perfil(request):
    return render(request, 'app/perfil.html')

def editar_perfil(request):
    return render(request, 'app/editar_perfil.html')

def historial_compra(request):
    return render(request, 'app/historial_compra.html')

def detalle_pedido(request):
    return render(request, 'app/detalle_pedido.html')

def add_producto(request):

    data = {

        'form': ProductoForm()

    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Videojuego agregado Correctamente")

            return redirect(to='productos_adm')
        else:
            data["form"] = formulario

    return render(request, 'app/add_producto.html', data)

def pedidos_adm(request):
    return render(request, 'app/pedidos_adm.html')

def usuarios_adm(request):
    return render(request, 'app/usuarios_adm.html')

def productos_adm(request):
    productos = Producto.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data={
        'productos': productos
    }


    return render(request, 'app/productos_adm.html', data)

def mod_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado Correctamente")
            data["mensaje"] = "Editado correctamente"
            return redirect(to="productos_adm")
        else:
            data["form"] = formulario

    return render(request, 'app/mod_producto.html', data)

def delete_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        producto.delete()
        messages.success(request, "Eliminado Correctamente")
        return redirect(to="productos_adm")
    return render(request, 'app/delete_producto.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        data["form"] = formulario
    
    return render(request, 'registration/registro.html', data)




