# Ejercicio 43 — Sistema de Inventario Inteligente

class Proveedor:
    def __init__(self, id_prov, nombre):
        self.id_prov = id_prov
        self.nombre = nombre

class OrdenCompra:
    def __init__(self, id_orden, proveedor, items):
        self.id_orden = id_orden
        self.proveedor = proveedor
        self.items = items

class Almacen:
    def __init__(self):
        self.productos = {}

    def recibir(self, producto, cantidad):
        self.productos[producto] = self.productos.get(producto, 0) + cantidad
        print(f"Recibido {cantidad} de {producto}. Stock actual: {self.productos[producto]}")

alm = Almacen()
alm.recibir("Sofá", 10)
alm.recibir("Sofá", 5)
alm.recibir("Almohadas", 100)
alm.recibir("Neveras", 25)
alm.recibir("Almohadas", 100)
alm.recibir("Neveras", 25)