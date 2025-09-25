# Ejercicio 45 — Sistema de Gestión Hospitalaria

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []

class Tratamiento:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

dep = Departamento("Cardiología")
t = Tratamiento("Cirugía", "Operación de corazón abierto")
dep.doctores.append("Dr. Juan")
print(f"Departamento: {dep.nombre}, Doctores: {dep.doctores}")
