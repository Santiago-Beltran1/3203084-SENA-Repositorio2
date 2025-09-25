# Ejercicio 26 — Sistema de Calificaciones

class Materia:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.inscritos = {}

    def inscribir(self, estudiante):
        self.inscritos[estudiante.id_est] = {"est": estudiante, "notas": []}

    def registrar_nota(self, id_est, nota):
        if id_est in self.inscritos:
            self.inscritos[id_est]["notas"].append(nota)

    def promedio_estudiante(self, id_est):
        notas = self.inscritos[id_est]["notas"]
        return sum(notas)/len(notas) if notas else 0

class EstudianteUni:
    def __init__(self, id_est, nombre):
        self.id_est = id_est
        self.nombre = nombre

mat = Materia("1", "Matemáticas", 3)
est = EstudianteUni(1, "Martha")
mat.inscribir(est)
mat.registrar_nota(1, 8)
mat.registrar_nota(1, 9)
print("Promedio Carlos:", mat.promedio_estudiante(1))
