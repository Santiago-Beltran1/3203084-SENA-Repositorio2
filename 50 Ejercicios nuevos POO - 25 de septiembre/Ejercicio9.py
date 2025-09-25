# Ejercicio 9 — Círculo Matemático

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio**2

    def circunferencia(self):
        return 2 * math.pi * self.radio

    def comparar(self, otro):
        return self.radio == otro.radio

c1 = Circulo(5)
c2 = Circulo(2)
print("Área 1:", c1.area())
print("Circunferencia 1:", c1.circunferencia())
print("Área 2:", c2.area())
print("Circunferencia 2:", c2.circunferencia())
print("¿Iguales?", c1.comparar(c2))
