# Ejercicio 50 — Metaverso Virtual

class Avatar:
    def __init__(self, id_av, nombre):
        self.id_av = id_av
        self.nombre = nombre
        self.pos = (0, 0, 0)
        self.inventario = []

class MundoVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.avatars = {}

    def agregar_avatar(self, avatar):
        self.avatars[avatar.id_av] = avatar
        print(f"Avatar {avatar.nombre} agregado al mundo {self.nombre}.")

class ObjetoVirtual:
    def __init__(self, id_obj, nombre, propiedades):
        self.id_obj = id_obj
        self.nombre = nombre
        self.propiedades = propiedades

mundo = MundoVirtual("Metaverso PC Santiago")
av1 = Avatar(1, "Jugador1")
av2 = Avatar(2, "Jugador2")
av3 = Avatar(3, "Jugador3")

mundo.agregar_avatar(av1)
mundo.agregar_avatar(av2)
mundo.agregar_avatar(av3)
