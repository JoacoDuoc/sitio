from django.shortcuts import render,  redirect, get_object_or_404
from .models import Producto ,User
from .forms import ProductoForm,CustomUserCreationForm,UpdProductoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import logout
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect
from app.Carrito import Carrito
from app.context_processor import total_carrito


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

    return render(request, 'app/index.html',data)

def recuperar_pswd(request):
    return render(request, 'app/recuperar_pswd.html')

def email_recuperar_pswd(request):
    return render(request, 'app/email_recuperar_pswd.html')

def detalle_game(request,id):
   producto=get_object_or_404(Producto,id=id)
   #persona=Persona.objects.get(rut=id) #None
   #print(persona)
   datos = {

        "producto":producto
    }
   
   return render(request,'app/detalle_game.html', datos)

def carrito(request):
    return render(request, 'app/carrito.html',)

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
    usuarios = User.objects.all()
    
    data={
        'usuarios': usuarios
    }
    return render(request, 'app/usuarios_adm.html',data)

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


@login_required()
def carro(request):
    cliente = User.objects.get(usuario_id = request.user.id)
    ctx = {
        "sub" : cliente.subscriptor
    }
    return render(request, "crud/carro.html", ctx)

@login_required()
def agregar(request, producto_id, pagina):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect(pagina)


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carro")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carro")

def sumar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.sumar(producto)
    return redirect("carro")
@login_required()    
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carro")
"""
@login_required()
def guardar(request):
    usuario = request.user
    tot_carrito = total_carrito(request)
    carrito = Carrito(request)
    total = tot_carrito["total_carrito"]
    cliente = User.objects.get(usuario_id = usuario.id)
    if cliente.subscriptor == True:
        total = tot_carrito["descuento"]
    ventas = Venta(cliente_id = cliente.id, total = total)
    ventas.save()
    venta_actual = Venta.objects.get(id = ventas.id)
    #guardar detalle
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            detalle = DetalleVenta(venta_id = venta_actual.id, producto_id = int(value["producto_id"]), cantidad = int(value["cantidad"]), precio = int(value["precio"]) )
            
            detalle.save()
            if cliente.subscriptor == False and int(value["producto_id"]) == 45:
                cliente.subscriptor = True
                cliente.save()
    carrito.limpiar()
    return redirect(perfil, 1)  
"""

