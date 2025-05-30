# tienda_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_productos, name='catalogo_productos'),
    path('agregar/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('actualizar_carrito/', views.actualizar_carrito, name='actualizar_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('colocar_pedido/', views.colocar_pedido, name='colocar_pedido'),
]