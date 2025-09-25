# Ejercicio 14 — Dado de Juego

import random

class Dado:
    def __init__(self, caras=6):
        self.caras = caras
        self.historial = []

    def lanzar(self):
        valor = random.randint(1, self.caras)
        self.historial.append(valor)
        return valor

    def estadisticas(self):
        return {
            "lanzamientos": len(self.historial),
            "suma": sum(self.historial)
        }

dado = Dado()
for _ in range(5):
    print("Lanzamiento:", dado.lanzar())
print("Estadísticas:", dado.estadisticas())
