# Ejercicio 33 — Sistema de Pedidos

from datetime import datetime

class Cliente:
    def __init__(self, id_cli, nombre):
        self.id_cli = id_cli
        self.nombre = nombre

class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.detalles = []
        self.estado = "Creado"
        self.fecha = datetime.now()

    def agregar_detalle(self, producto, cantidad, precio):
        self.detalles.append({"producto": producto, "cantidad": cantidad, "precio": precio})

    def total(self):
        return sum(d["cantidad"] * d["precio"] for d in self.detalles)

cli = Cliente(1, "Luis")
pedido = Pedido(1, cli)
pedido.agregar_detalle("buzo", 2, 50)
pedido.agregar_detalle("gorra", 1, 100)
print("Total del pedido:", pedido.total())
