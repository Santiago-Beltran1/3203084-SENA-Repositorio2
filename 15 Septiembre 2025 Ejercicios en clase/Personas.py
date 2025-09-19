#Ejercicio 1
class personas:
    def __init__(self, nombre, genero, ocupacion):
        self.nombre = nombre
        self.genero= genero
        self.ocupacion = ocupacion

persona1 = personas("Pepito Peréz", "Maculino", "Administrador")
persona2 = personas("Pepita Peréz", "Femenino", "Programadora")

print(persona1.nombre, persona1.genero, persona1.ocupacion)
print(persona2.nombre, persona2.genero, persona2.ocupacion)