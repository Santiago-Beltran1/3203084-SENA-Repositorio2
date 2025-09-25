# Ejercicio 38 — Plataforma de Cursos Online

class Curso:
    def __init__(self, codigo, nombre, instructor):
        self.codigo = codigo
        self.nombre = nombre
        self.instructor = instructor
        self.modulos = []

class Modulo:
    def __init__(self, nombre, orden):
        self.nombre = nombre
        self.orden = orden
        self.lecciones = []

class Leccion:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

curso = Curso("C1", "Excel", "Karina")
mod = Modulo("Introducción", 1)
lec = Leccion("Bienvenida", "Contenido de bienvenida")
mod.lecciones.append(lec)
curso.modulos.append(mod)
print("Curso:", curso.nombre, "Módulos:", [m.nombre for m in curso.modulos])
