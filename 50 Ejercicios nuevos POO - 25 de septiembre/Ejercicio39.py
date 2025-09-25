# Ejercicio 39 — Sistema de Gestión de Proyectos

from datetime import datetime

class TareaProyecto:
    def __init__(self, nombre, fecha_limite):
        self.nombre = nombre
        self.fecha_creacion = datetime.now()
        self.fecha_limite = fecha_limite
        self.estado = "Pendiente"

class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

proy = Proyecto("App Web")
tarea = TareaProyecto("Diseñar interfaz", "2025-10-15")
proy.agregar_tarea(tarea)
print("Tareas del proyecto:", [t.nombre for t in proy.tareas])
