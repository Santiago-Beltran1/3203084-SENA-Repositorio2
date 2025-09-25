# 28. Biblioteca Digital

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.prestamos = {}

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def prestar_libro(self, usuario, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                self.prestamos[usuario] = titulo
                print(f"{usuario} ha prestado {titulo}")
                return
        print("Libro no disponible")

    def devolver_libro(self, usuario):
        if usuario in self.prestamos:
            titulo = self.prestamos[usuario]
            for libro in self.libros:
                if libro.titulo == titulo:
                    libro.disponible = True
                    break
            del self.prestamos[usuario]
            print(f"{usuario} devolvió {titulo}")

biblio = Biblioteca()
biblio.agregar_libro(Libro("Python"))
biblio.agregar_libro(Libro("Repositorio del SENA"))

while True:
    print("\n1. Prestar libro\n2. Devolver libro\n3. Ver préstamos\n4. Salir")
    op = input("Opción: ")
    if op == "1":
        usuario = input("Usuario: ")
        titulo = input("Título: ")
        biblio.prestar_libro(usuario, titulo)
    elif op == "2":
        usuario = input("Usuario: ")
        biblio.devolver_libro(usuario)
    elif op == "3":
        print(biblio.prestamos)
    elif op == "4":
        break
    else:
        print("Opción inválida")
