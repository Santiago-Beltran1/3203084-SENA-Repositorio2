# Ejercicio 42 — Plataforma de Streaming

class Contenido:
    def __init__(self, id_cont, titulo, duracion):
        self.id_cont = id_cont
        self.titulo = titulo
        self.duracion = duracion

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.items = []

    def agregar(self, contenido):
        self.items.append(contenido)
        print(f"Contenido '{contenido.titulo}' agregado a la playlist.")

class Suscripcion:
    def __init__(self, usuario, tipo):
        self.usuario = usuario
        self.tipo = tipo

p = Playlist("Favoritos")
c1 = Contenido(1, "Película A", "120 min")
p.agregar(c1)
