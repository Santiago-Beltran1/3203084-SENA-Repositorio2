# Ejercicio 5 — Estudiante y Calificaciones

class EstudianteNotas:
    def __init__(self, id_est, nombre_est):
        self.id_est = id_est
        self.nombre_est = nombre_est
        self._notas = []

    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self._notas.append(nota)
            print(f"Nota {nota} agregada.")
        else:
            print("La nota debe estar entre 0 y 10.")

    def promedio(self):
        if self._notas:
            return sum(self._notas) / len(self._notas)
        return 0

est = EstudianteNotas(1, "Ana")
est.agregar_nota(8)
est.agregar_nota(9)
print("Promedio:", est.promedio())