from django.urls import path, include

from .views import index, login, registrarse, recuperar_pswd, email_recuperar_pswd, detalle_game, carrito, pago, finpago, filtro, favs, perfil, editar_perfil, historial_compra, detalle_pedido, add_producto, pedidos_adm, usuarios_adm, productos_adm

#URLS APP
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('registrarse/', registrarse, name='registrarse'),
    path('recuper_pswd/', recuperar_pswd, name='recuperar_pswd'),
    path('email_recuperar_pswd/', email_recuperar_pswd, name='email_recuperar_pswd'),
    path('detalle_game/', detalle_game, name='detalle_game'),
    path('carrito/', carrito, name='carrito'),
    path('pago/', pago, name='pago'),
    path('finpaga/', finpago, name='finpago'),
    path('filtro/', filtro, name='filtro'),
    path('favortios/', favs, name='favs'),
    path('perfil/', perfil, name='perfil'),
    path('edit_perfil/', editar_perfil, name='editar_perfil'),
    path('historial_compra/', historial_compra, name='historial_compra'),
    path('detalle_pedido/', detalle_pedido, name='detalle_pedido'),
    path('add_producto/', add_producto, name='add_producto'),
    path('pedidos_adm/', pedidos_adm, name='pedidos_adm'),
    path('usuarios_adm/', usuarios_adm, name='usuarios_adm'),
    path('productos_adm/', productos_adm, name='productos_adm'),
]