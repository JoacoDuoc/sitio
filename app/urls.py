from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import index, registro,  detalle_game, carrito, pago, finpago \
                 , filtro, favs, perfil, historial_compra, detalle_pedido, add_producto, pedidos_adm, usuarios_adm, \
                 productos_adm, mod_producto, delete_producto,salir, actualizarCarrito, agregar_al_carrito, eliminar_del_carrito, \
                 quitar_del_carrito, ver_carrito, detalle_boleta,compra, agregar_a_lista , eliminar_de_lista ,delete_usuarios, \
                actualizar_estado_boleta , cambiar_contraseña
#URLS APP
urlpatterns = [
    path('', index, name='index'),
    path('detalle_game/<id>/', detalle_game, name='detalle_game'),
    path('carrito/', carrito, name='carrito'),
    path('pago/', pago, name='pago'),
    path('finpago/', finpago, name='finpago'),
    path('filtro/', filtro, name='filtro'),
    path('favs/', favs, name='favs'),
    path('agregar/<int:producto_id>/', agregar_a_lista, name='agregar_a_lista'),
    path('eliminar/<int:producto_id>/', eliminar_de_lista, name='eliminar_de_lista'),
    path('perfil/<id>', perfil, name='perfil'),
    path('historial_compra/', historial_compra, name='historial_compra'),
    path('detalle_pedido/', detalle_pedido, name='detalle_pedido'),
    path('add_producto/', add_producto, name='add_producto'),
    path('pedidos_adm/', pedidos_adm, name='pedidos_adm'),
    path('usuarios_adm/', usuarios_adm, name='usuarios_adm'),
    path('delete_usuarios/<id>/', delete_usuarios, name='delete_usuarios'),
    path('productos_adm/', productos_adm, name='productos_adm'),
    path('mod_producto/<id>/', mod_producto, name='mod_producto'),
    path('delete_producto/<id>/', delete_producto, name='delete_producto'),
    path('salir/',salir,name='salir'),
    path('registro/', registro, name="registro"),
    path('actualizar_carrito/', actualizarCarrito, name='actualizar_carrito'),
    path('agregar-al-carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('quitar-del-carrito/<int:producto_id>/', quitar_del_carrito, name='quitar_del_carrito'),
    path('eliminar-del-carrito/<int:producto_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('ver-carrito/', ver_carrito, name='ver_carrito'),
    path('detalle_boleta/<id>', detalle_boleta, name='detalle_boleta'),
    path('compra/<int:producto_id>/', compra, name='compra'),
    path('actualizar_estado_boleta/<uuid:boleta_id>/', actualizar_estado_boleta, name='actualizar_estado_boleta'),
    path('cambiar-contraseña/', cambiar_contraseña, name='cambiar_contraseña'),

]