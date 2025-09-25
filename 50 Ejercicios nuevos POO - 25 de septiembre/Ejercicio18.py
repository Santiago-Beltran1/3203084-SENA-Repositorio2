# Ejercicio 18 — Formas Geométricas con Herencia

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return 0.5 * self.base * self.altura

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

t = Triangulo(10, 5)
c = Cuadrado(4)
print("Área Triángulo:", t.area())
print("Área Cuadrado:", c.area())
