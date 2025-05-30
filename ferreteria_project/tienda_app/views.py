# tienda_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Producto, Cliente, Carrito, Pedido
from django.http import HttpResponseRedirect

def catalogo_productos(request):
    productos = Producto.objects.all()

    # Obtener el cliente para el carrito (manteniendo el cliente anónimo por ahora)
    cliente_nombre = "Cliente Anónimo"
    cliente, created = Cliente.objects.get_or_create(nombre_cliente=cliente_nombre)
    if created:
        cliente.correo = f"{cliente_nombre.replace(' ', '').lower()}@example.com"
        cliente.save()

    # Contar los ítems en el carrito para el cliente actual
    # Esto cuenta el número de entradas distintas en el carrito, no la cantidad total de productos
    # Si quieres la suma de las cantidades de productos, usa sum(item.cantidad for item in Carrito.objects.filter(cliente=cliente))
    cantidad_items_carrito = Carrito.objects.filter(cliente=cliente).count()


    context = {
        'productos': productos,
        'carrito_url': reverse('ver_carrito'),
        'cantidad_items_carrito': cantidad_items_carrito, # Pasar la cantidad de ítems al contexto
    }
    return render(request, 'tienda_app/catalogo.html', context)

def agregar_al_carrito(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cantidad = int(request.POST.get('cantidad', 1))
        producto = get_object_or_404(Producto, pk=product_id)

        cliente_nombre = "Cliente Anónimo"
        cliente, created = Cliente.objects.get_or_create(nombre_cliente=cliente_nombre)
        if created:
            cliente.correo = f"{cliente_nombre.replace(' ', '').lower()}@example.com"
            cliente.save()

        carrito_item, created = Carrito.objects.get_or_create(cliente=cliente, producto=producto)

        if not created:
            carrito_item.cantidad += cantidad
        else:
            carrito_item.cantidad = cantidad
        carrito_item.save()

        # ***** CAMBIO CLAVE AQUÍ: REDIRIGIR DE VUELTA AL CATÁLOGO *****
        return redirect('catalogo_productos') # Redirigimos al catálogo
    return redirect('catalogo_productos') # Si es un GET request, también al catálogo

def ver_carrito(request):
    cliente_nombre = "Cliente Anónimo"
    cliente, created = Cliente.objects.get_or_create(nombre_cliente=cliente_nombre)
    if created:
        cliente.correo = f"{cliente_nombre.replace(' ', '').lower()}@example.com"
        cliente.save()

    carrito_items = Carrito.objects.filter(cliente=cliente)

    total_carrito_monto = 0
    # Calculate subtotal for each item and total for the cart
    for item in carrito_items:
        item.subtotal = item.producto.precio * item.cantidad # Calculate subtotal here
        total_carrito_monto += item.subtotal

    context = {
        'carrito_items': carrito_items,
        'total_carrito_monto': total_carrito_monto,
    }
    return render(request, 'tienda_app/carrito.html', context)

def actualizar_carrito(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        cantidad = int(request.POST.get('cantidad', 1))

        if cantidad <= 0:
            return redirect('eliminar_del_carrito', item_id=item_id)

        carrito_item = get_object_or_404(Carrito, pk=item_id)
        carrito_item.cantidad = cantidad
        carrito_item.save()
        return redirect('ver_carrito')
    return redirect('ver_carrito')

def eliminar_del_carrito(request, item_id):
    carrito_item = get_object_or_404(Carrito, pk=item_id)
    carrito_item.delete()
    return redirect('ver_carrito')

def colocar_pedido(request):
    cliente_nombre = "Cliente Anónimo"
    cliente, created = Cliente.objects.get_or_create(nombre_cliente=cliente_nombre)
    if created:
        cliente.correo = f"{cliente_nombre.replace(' ', '').lower()}@example.com"
        cliente.save()

    carrito_items = Carrito.objects.filter(cliente=cliente)
    monto_total_pedido = 0

    if carrito_items:
        for item in carrito_items:
            monto_total_pedido += item.producto.precio * item.cantidad

        first_cart_item = carrito_items.first()
        if first_cart_item:
            pedido = Pedido.objects.create(
                cliente=cliente,
                producto=first_cart_item.producto,
                monto=monto_total_pedido,
                direccion_envio='Dirección de Envío Pendiente',
                estatus='pendiente'
            )
        else:
            return render(request, 'tienda_app/carrito_vacio.html')

        Carrito.objects.filter(cliente=cliente).delete()

        return render(request, 'tienda_app/pedido_exitoso.html', {'monto_total': monto_total_pedido, 'pedido_id': pedido.id})
    else:
        return render(request, 'tienda_app/carrito_vacio.html')