# Ejercicio 31 — Sistema de Transporte

class Parada:
    def __init__(self, id_parada, nombre):
        self.id_parada = id_parada
        self.nombre = nombre

class Ruta:
    def __init__(self, numero, nombre, paradas):
        self.numero = numero
        self.nombre = nombre
        self.paradas = paradas

    def siguiente(self, parada_actual):
        if parada_actual in self.paradas:
            idx = self.paradas.index(parada_actual)
            if idx + 1 < len(self.paradas):
                return self.paradas[idx + 1]
        return None

class Bus:
    def __init__(self, numero, ruta, cap=40):
        self.numero = numero
        self.ruta = ruta
        self.cap = cap
        self.pasajeros = []

p1 = Parada(1, "Centro")
p2 = Parada(2, "Norte")
p3 = Parada(3, "Sur")
ruta = Ruta(101, "Principal", [p1, p2, p3])
print("Siguiente parada:", ruta.siguiente(p1).nombre)
