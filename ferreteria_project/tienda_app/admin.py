# tienda_app/admin.py
from django.contrib import admin
from .models import Categoria, Producto, Cliente, Carrito, Pedido

# Personalización básica para mostrar más campos en la lista del admin (opcional)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'imagen')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'categoria__nombre')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'correo', 'telefono')
    search_fields = ('nombre_cliente', 'correo')

class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'producto', 'cantidad', 'fecha_agregado')
    list_filter = ('cliente', 'producto')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'producto', 'monto', 'fecha_pedido', 'direccion_envio') # Considera añadir un campo 'estado' aquí más adelante
    list_filter = ('cliente',)
    search_fields = ('cliente__nombre_cliente', 'producto__nombre')

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Pedido, PedidoAdmin)