# Ejercicio 48 — Simulador de Ecosistema

import random

class SerVivo:
    def __init__(self, nombre, energia=100):
        self.nombre = nombre
        self.energia = energia
        self.vivo = True

    def moverse(self):
        self.energia -= 5
        print(f"{self.nombre} se movió. Energía: {self.energia}")

class Planta(SerVivo):
    def fotosintesis(self):
        ganancia = random.randint(5, 15)
        self.energia += ganancia
        print(f"{self.nombre} hizo fotosíntesis. Energía: {self.energia}")

class Animal(SerVivo):
    def comer(self, alimento):
        if isinstance(alimento, Planta) and alimento.vivo:
            self.energia += 20
            alimento.vivo = False
            print(f"{self.nombre} comió {alimento.nombre}. Energía: {self.energia}")

p = Planta("Rosa")
a = Animal("Conejo")
p.fotosintesis()
a.comer(p)
