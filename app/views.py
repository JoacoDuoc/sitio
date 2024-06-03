from django.shortcuts import render

# Create your views here.\
def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/login.html')

def registrarse(request):
    return render(request, 'app/registrarse.html')

def recuperar_pswd(request):
    return render(request, 'app/recuperar_pswd.html')

def email_recuperar_pswd(request):
    return render(request, 'app/email_recuperar_pswd.html')

def detalle_game(request):
    return render(request, 'app/detalle_game.html')

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
    return render(request, 'app/add_producto.html')

def pedidos_adm(request):
    return render(request, 'app/pedidos_adm.html')

def usuarios_adm(request):
    return render(request, 'app/usuarios_adm.html')

def productos_adm(request):
    return render(request, 'app/productos_adm.html')

