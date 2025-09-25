# 23. Juego de Cartas

import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Baraja:
    def __init__(self):
        palos = ["Corazones", "Diamantes", "Tréboles", "Espadas"]
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cartas = [Carta(v, p) for p in palos for v in valores]

    def mezclar(self):
        random.shuffle(self.cartas)

    def repartir(self, jugadores, cartas_por_jugador):
        manos = {f"Jugador {i+1}": [] for i in range(jugadores)}
        for _ in range(cartas_por_jugador):
            for j in manos:
                manos[j].append(self.cartas.pop())
        return manos

baraja = Baraja()
baraja.mezclar()
jug = int(input("Número de jugadores: "))
cartas = int(input("Cartas por jugador: "))
manos = baraja.repartir(jug, cartas)

for jugador, cartas in manos.items():
    print(jugador, ":", [str(c) for c in cartas])
