# Ejercicio 27 — Red Social Básica

from datetime import datetime

class UsuarioRed:
    def __init__(self, username, email, nombre):
        self.username = username
        self.email = email
        self.nombre = nombre
        self.seguidores = set()
        self.siguiendo = set()
        self.publicaciones = []

    def seguir(self, otro):
        if otro.username != self.username:
            self.siguiendo.add(otro.username)
            otro.seguidores.add(self.username)

    def publicar(self, contenido):
        post = {"autor": self.username, "contenido": contenido, "fecha": datetime.now()}
        self.publicaciones.append(post)
        print(f"{self.username} publicó: {contenido}")

u1 = UsuarioRed("julián", "j@ej.com", "Julián")
u2 = UsuarioRed("alejandra", "a@ej.com", "Alejandra")
u1.seguir(u2)
u2.publicar("Hola, Quiero Seguirte!")
