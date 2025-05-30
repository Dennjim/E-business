from django.db import models
# from django.utils import timezone # No se usó timezone explícitamente, pero auto_now_add lo maneja

class Categoria(models.Model):
    nombre = models.CharField(max_length=45)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    imagen = models.CharField(max_length=255, null=True, blank=True, db_column='imagen')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='categoria_id')

    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.AutoField(primary_key=True, db_column='Idclientes')
    correo = models.CharField(max_length=45, unique=True)
    nombre_cliente = models.CharField(max_length=45, db_column='nombredelcliente')
    direccion_envio = models.CharField(max_length=255, null=True, blank=True, db_column='direccion_de_envio')
    telefono = models.CharField(max_length=45, null=True, blank=True)
    clientescol = models.CharField(max_length=45, null=True, blank=True)
    telefonocol = models.CharField(max_length=45, null=True, blank=True)
    clientescol1 = models.BinaryField(null=True, blank=True)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return self.nombre_cliente

class Carrito(models.Model):
    id = models.AutoField(primary_key=True, db_column='idCarrito')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='idProducto')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='idCliente')
    cantidad = models.IntegerField(default=1)
    fecha_agregado = models.DateTimeField(auto_now_add=True, db_column='fechaAgregado')

    class Meta:
        db_table = 'carrito'
        unique_together = (('producto', 'cliente'),)

    def __str__(self):
        return f"Carrito {self.id} - {self.cliente.nombre_cliente} - {self.producto.nombre}"

class Pedido(models.Model):
    id = models.AutoField(primary_key=True, db_column='Idcliente_pedido')
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    direccion_envio = models.CharField(max_length=255, null=True, blank=True, db_column='direccion_envio')
    fecha_pedido = models.DateTimeField(null=True, blank=True, db_column='fechapedido')
    pedidoscol = models.CharField(max_length=45, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='clientes_idclientes')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='productos_ID_INT')
    estatus = models.CharField(max_length=50, default='pendiente') # <--- Make sure this line exists!


    class Meta:
        db_table = 'pedidos'

    def __str__(self):
        return f"Pedido {self.id} por {self.cliente.nombre_cliente}"