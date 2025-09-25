# Ejercicio 15 — Semáforo de Tráfico

class Semaforo:
    SECUENCIA = ["rojo", "amarillo", "verde"]

    def __init__(self):
        self._idx = 0

    def siguiente(self):
        self._idx = (self._idx + 1) % len(self.SECUENCIA)
        return self.estado()

    def estado(self):
        return self.SECUENCIA[self._idx]

semaforo = Semaforo()
for _ in range(5):
    print("Estado:", semaforo.estado())
    semaforo.siguiente()
