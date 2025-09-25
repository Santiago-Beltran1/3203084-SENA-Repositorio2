# Ejercicio 12 — Libro de Biblioteca

from datetime import datetime

class Libro:
    def __init__(self, isbn, titulo, autor, año):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = True
        self.fecha_prestamo = None
        self.usuario_actual = None

    def prestar(self, usuario):
        if self.disponible:
            self.disponible = False
            self.fecha_prestamo = datetime.now()
            self.usuario_actual = usuario
            print(f"Libro '{self.titulo}' prestado a {usuario}")
        else:
            print("El libro no está disponible.")

    def devolver(self):
        if not self.disponible:
            print(f"Libro '{self.titulo}' devuelto por {self.usuario_actual}")
            self.disponible = True
            self.fecha_prestamo = None
            self.usuario_actual = None

libro = Libro("1", "Cóndores no matan todos los días", "Gustavo Gardeazabal", 1971)
libro2 = Libro("2", "Luna de Plutón", "Anónimo", 2022)
libro.prestar("Carlos")
libro.devolver()
