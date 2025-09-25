# Ejercicio 44 — Simulador de Bolsa de Valores

import random

class Accion:
    def __init__(self, ticker, precio):
        self.ticker = ticker
        self.precio = precio

    def actualizar_precio(self):
        self.precio *= (1 + random.uniform(-0.05, 0.05))
        print(f"Nuevo precio de {self.ticker}: {self.precio:.2f}")

class Portafolio:
    def __init__(self):
        self.posiciones = {}

    def comprar(self, accion, cantidad):
        self.posiciones[accion.ticker] = self.posiciones.get(accion.ticker, 0) + cantidad
        print(f"Compradas {cantidad} acciones de {accion.ticker}")

a = Accion("AAPL", 150)
a.actualizar_precio()
p = Portafolio()
p.comprar(a, 10)
