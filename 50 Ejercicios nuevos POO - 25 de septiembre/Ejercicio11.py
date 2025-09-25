# Ejercicio 11 — Reloj Digital

class Reloj:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.segundos_totales = horas*3600 + minutos*60 + segundos

    def avanzar(self, segundos):
        self.segundos_totales = (self.segundos_totales + segundos) % (24*3600)

    def mostrar_24h(self):
        h = self.segundos_totales // 3600
        m = (self.segundos_totales % 3600) // 60
        s = self.segundos_totales % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

reloj = Reloj(23, 59, 50)
for _ in range(15):
    reloj.avanzar(1)
    print(reloj.mostrar_24h())
