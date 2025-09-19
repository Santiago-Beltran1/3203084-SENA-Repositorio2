#Ejercicio 2
class alumnos:
    def __init__(self, nombre, edad, programa):
        self.nombre = nombre
        self.edad= edad
        self.programa = programa

alumno1 = alumnos("Pepito Peréz", "15 años", "Ganadería")
alumno2 = alumnos("Pepita Peréz", "18 años", "Deportes")

print(alumno1.nombre, alumno1.edad, alumno1.programa)
print(alumno2.nombre, alumno2.edad, alumno2.programa)