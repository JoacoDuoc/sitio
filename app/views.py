from django.shortcuts import render,  redirect, get_object_or_404
from .models import Producto, Boleta, Detalle_boleta
from .forms import ProductoForm,CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import logout 
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
import json
from django.http import JsonResponse , HttpResponse

# Create your views here.\
def salir(request):
    logout(request)
    messages.info(request,'Sesion Cerrada')
    return redirect(to="index")


def index(request):
    productos = Producto.objects.all()
    page = request.GET.get('page',1)

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

@login_required
def pago(request):
    
    order,creada = Boleta.objects.get_or_create(cliente=request.user,completada=False)
    items = order.detalle_boleta_set.all()
    items_carrito = order.get_item

    if items.count() <= 0:
        return redirect('index')
    
    if request.method == 'POST':
        order.completada = True 
        order.save()
        messages.success(request,"Procesada con éxito")

    context = {'items': items, 'order' : order}   
    return render(request,"app/pago.html", context)

@login_required
@permission_required("pagina.view_user",raise_exception=True)
def detalle_boleta(request,id):
    boleta = Boleta.objects.get(id=id)
    productos = Detalle_boleta.objects.filter(boleta=boleta)
    context = {'boleta':boleta,'productos':productos}
    return render(request,"app/detalle_boleta.html", context)


@login_required
def carrito(request):
    order, created = Boleta.objects.get_or_create(cliente=request.user, completada=False)
    items = order.detalle_boleta_set.all()
    items_carrito = order.get_item  # Asegúrate de tener este método o propiedad definido en el modelo Boleta

    data = {
        'order': order,
        'items': items,
        'items_carrito': items_carrito,
    }

    return render(request, 'app/carrito.html', data)

@require_POST
def actualizarCarrito(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    producto = Producto.objects.get(id=productId)
    order,creada = Boleta.objects.get_or_create(cliente=request.user,completada=False)
    detalle_orden,creada = Detalle_boleta.objects.get_or_create(boleta=order,producto=producto)
    if action == 'add':
        if detalle_orden.cantidad_productos < producto.stock: 
            detalle_orden.cantidad_productos +=1
    elif action == 'remove': 
        detalle_orden.cantidad_productos -=1
    
    elif action == 'delete':
        detalle_orden.cantidad_productos = 0    
    detalle_orden.save()          
    if detalle_orden.cantidad_productos <= 0: 
        detalle_orden.delete()
    return JsonResponse("Carrito actualizado",safe=False) 

def finpago(request):
    return render(request, 'app/finpago.html')

def filtro(request):
    return render(request, 'app/filtro.html')

@login_required
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
    boletas = Boleta.objects.filter(completada=True)
    data = {'boletas': boletas}
    return render(request,"app/pedidos_adm.html",data) 

def usuarios_adm(request):
    usuarios= User.objects.all()

    datos={

        "usuarios":usuarios

    }

    return render(request, 'app/usuarios_adm.html', datos)

def productos_adm(request):
    productos = Producto.objects.all()
    page = request.GET.get('page',1)

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

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    order, created = Boleta.objects.get_or_create(cliente=request.user, completada=False)
    detalle_orden, created = Detalle_boleta.objects.get_or_create(boleta=order, producto=producto)
    detalle_orden.cantidad_productos += 1
    detalle_orden.save()
    return redirect('carrito')

@login_required
def quitar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    order = Boleta.objects.get(cliente=request.user, completada=False)
    detalle_orden = Detalle_boleta.objects.get(boleta=order, producto=producto)
    if detalle_orden.cantidad_productos > 1:
        detalle_orden.cantidad_productos -= 1
        detalle_orden.save()
    else:
        detalle_orden.delete()
    return redirect('carrito')

@login_required
def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    order = Boleta.objects.get(cliente=request.user, completada=False)
    detalle_orden = Detalle_boleta.objects.get(boleta=order, producto=producto)
    detalle_orden.delete()
    return redirect('carrito')

@login_required
def ver_carrito(request):
    order = Boleta.objects.filter(cliente=request.user, completada=False).first()
    context = {
        'order': order
    }
    return render(request, 'carrito.html', context)


@login_required
def compra(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    order, created = Boleta.objects.get_or_create(cliente=request.user, completada=False)
    detalle_orden, created = Detalle_boleta.objects.get_or_create(boleta=order, producto=producto)
    detalle_orden.cantidad_productos += 1
    detalle_orden.save()
    return redirect('pago')

