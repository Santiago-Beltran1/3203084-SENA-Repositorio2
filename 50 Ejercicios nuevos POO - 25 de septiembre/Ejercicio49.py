# Ejercicio 49 — Sistema de Inteligencia Artificial

class Neurona:
    def __init__(self, peso=1.0):
        self.peso = peso

    def activar(self, entrada):
        return 1 if entrada * self.peso > 0.5 else 0

class RedSimple:
    def __init__(self, neuronas):
        self.neuronas = neuronas

    def predecir(self, entradas):
        return [n.activar(sum(entradas)) for n in self.neuronas]

n1 = Neurona(0.2)
n2 = Neurona(0.8)
red = RedSimple([n1, n2])
print("Predicción:", red.predecir([1, 2, 3]))
