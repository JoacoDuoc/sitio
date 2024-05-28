from django.urls import path, include

from .views import index, login, register, recuperar_pswd, email_recuperar_pwsd, detalle_game, carrito, pago, finpago, filtro, favs, perfil, editar_perfil, historial, detalle_pedido, add_producto, pedidos_adm, usuarios_adm, productos_adm

#URLS APP
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('recuper_pswd/', recuperar_pswd, name='recuperar_pswd'),
    path('emailenviado/', email_recuperar_pwsd, name='email_recuperar_pwsd'),
    path('detallejuego/', detalle_game, name='detalle_game'),
    path('carrito/', carrito, name='carrito'),
    path('pago/', pago, name='pago'),
    path('finpaga/', finpago, name='finpago'),
    path('filtro/', filtro, name='filtro'),
    path('favortios/', favs, name='favs'),
    path('perfil/', perfil, name='perfil'),
    path('editperfil/', editar_perfil, name='editar_perfil'),
    path('historial/', historial, name='historial'),
    path('detallepedido/', detalle_pedido, name='detalle_pedido'),
    path('addproducto/', add_producto, name='add_producto'),
    path('pedidosadm/', pedidos_adm, name='pedidos_adm'),
    path('usuariosadm/', usuarios_adm, name='usuarios_adm'),
    path('productosadm/', productos_adm, name='prodcutos_adm'),
]