# Ejercicio 13 — Temperatura Convertidor

class Temperatura:
    def __init__(self, valor, unidad="C"):
        self.valor = valor
        self.unidad = unidad.upper()

    def a_celsius(self):
        if self.unidad == "C": return self.valor
        if self.unidad == "F": return (self.valor - 32) * 5/9
        if self.unidad == "K": return self.valor - 273.15

    def a_fahrenheit(self):
        return self.a_celsius() * 9/5 + 32

    def a_kelvin(self):
        return self.a_celsius() + 273.15

temp = Temperatura(100, "F")
print("En Celsius:", temp.a_celsius())
print("En Kelvin:", temp.a_kelvin())
