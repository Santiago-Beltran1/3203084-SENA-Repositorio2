#Generar un nombre de usuario 

class GeneradorUsuario:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def crear_usuario(self):
        return f"{self.nombre.lower()}{self.anio[-2:]}_nuevo"

nombre = input("Ingresa tu nombre: ")
anio = input("Ingresa tu año de nacimiento: ")
usuario = GeneradorUsuario(nombre, anio)
print(f"Tu nuevo nombre de usuario es: {usuario.crear_usuario()}")
