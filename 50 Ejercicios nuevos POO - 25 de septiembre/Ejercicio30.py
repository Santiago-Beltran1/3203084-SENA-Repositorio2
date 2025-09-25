# Ejercicio 30 — Juego RPG Básico

import random

class Personaje:
    def __init__(self, nombre, clase_p):
        self.nombre = nombre
        self.clase_p = clase_p
        self.nivel = 1
        self.vida = 100
        self.ataque = 10
        self.defensa = 5

    def atacar(self, objetivo):
        dano = max(1, self.ataque + random.randint(0, 6) - objetivo.defensa)
        objetivo.vida = max(0, objetivo.vida - dano)
        print(f"{self.nombre} atacó a {objetivo.nombre} causando {dano} de daño.")

    def esta_vivo(self):
        return self.vida > 0

p1 = Personaje("Héroe", "Guerrero")
p2 = Personaje("Orco", "Monstruo")
p1.atacar(p2)
p2.atacar(p1)
print("Vida Orco:", p2.vida)
print("Vida Héroe:", p1.vida)

