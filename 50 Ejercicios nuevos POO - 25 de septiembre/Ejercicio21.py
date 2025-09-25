# Ejercicio 21 — Carrito de Compras

class ProductoCarrito:
    def __init__(self, id_prod, nombre, precio, stock):
        self.id_prod = id_prod
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class ItemCarrito:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad

class CarritoCompras:
    def __init__(self, usuario):
        self.usuario = usuario
        self.items = []

    def agregar(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.items.append(ItemCarrito(producto, cantidad))
            print(f"Producto {producto.nombre} agregado.")
        else:
            print("Stock insuficiente.")

    def total(self):
        return sum(i.subtotal() for i in self.items)

p1 = ProductoCarrito(1, "Computador Pórtatil", 3000000, 5)
p2 = ProductoCarrito(1, "Celular", 800000, 10)
carrito = CarritoCompras("Juan")
carrito.agregar(p1, 2)
carrito.agregar(p2, 2)
print("Total a pagar:", carrito.total())
