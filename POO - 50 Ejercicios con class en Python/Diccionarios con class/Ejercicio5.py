#Gestionador de empleados

class RegistroEmpleados:
    def __init__(self):
        self.empleados = {}

    def agregEmpleado(self, nombre, sueldo):
        self.empleados[nombre] = sueldo

    def buscEmpleado(self, nombre):
        if nombre in self.empleados:
            print(f"{nombre} gana ${self.empleados[nombre]}")
        else:
            print("Empleado no encontrado.")

    def mostrar(self):
        print("\nLista de empleados:")
        for nombre, sueldo in self.empleados.items():
            print(f"{nombre}: ${sueldo}")


reg = RegistroEmpleados()

while True:
    print("\n--- EMPLEADOS ---")
    print("1. Agregar empleado")
    print("2. Buscar empleado")
    print("3. Ver todos")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del empleado: ")
        sueldo = float(input("Sueldo del empleado: "))
        reg.agregEmpleado(nombre, sueldo)
    elif opcion == "2":
        nombre = input("Nombre del empleado a buscar: ")
        reg.buscEmpleado(nombre)
    elif opcion == "3":
        reg.mostrar()
    elif opcion == "4":
        break
    else:
        print("Opción no válida")
