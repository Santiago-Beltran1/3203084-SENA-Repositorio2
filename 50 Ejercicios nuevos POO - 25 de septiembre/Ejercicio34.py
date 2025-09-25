# Ejercicio 34 — Escuela de Música

class EstudianteMus:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

class ProfesorMus:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clases = []

class ClaseMus:
    def __init__(self, nombre, instructor):
        self.nombre = nombre
        self.instructor = instructor
        self.inscritos = []

    def inscribir(self, est):
        self.inscritos.append(est)
        est.instrumentos.append(self.nombre)

prof = ProfesorMus("Carlos")
clase = ClaseMus("Guitarra", prof)
est = EstudianteMus("Ana")
clase.inscribir(est)
print("Instrumentos de Ana:", est.instrumentos)
