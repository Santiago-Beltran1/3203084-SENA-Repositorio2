# 22. Sistema de Usuarios

class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def mostrar_info(self):
        print(f"Usuario: {self.nombre}, Rol: {self.rol}")

usuarios = []

while True:
    print("\n1. Registrar usuario\n2. Ver usuarios\n3. Salir")
    op = input("Opción: ")
    if op == "1":
        nombre = input("Nombre: ")
        rol = input("Rol (Administrador/Cliente/Moderador): ")
        usuarios.append(Usuario(nombre, rol))
    elif op == "2":
        for u in usuarios:
            u.mostrar_info()
    elif op == "3":
        break
    else:
        print("Opción inválida")
