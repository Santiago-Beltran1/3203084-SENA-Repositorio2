# Ejercicio 40 — Red Social Avanzada

class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = set()
        self.eventos = []

class Evento:
    def __init__(self, titulo, fecha):
        self.titulo = titulo
        self.fecha = fecha
        self.asistentes = set()

class Notificacion:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

g = Grupo("Amigos")
g.miembros.add("PABLO")
e = Evento("Reunión", "2025-11-01")
g.eventos.append(e)
print("Miembros del grupo:", g.miembros)
