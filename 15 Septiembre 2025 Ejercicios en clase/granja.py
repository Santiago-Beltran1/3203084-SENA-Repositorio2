#Ejercicio 4
class granja:
    def __init__(self, nombre, tamaño, ubicacion, animales):
        self.nombre = nombre
        self.tamaño= tamaño
        self.ubicacion = ubicacion
        self.animales = animales

granja1 = granja("AgroU", "1000 hectáreas", "CBA Mosquera", "vacas, porcinos, cabras")
granja2 = granja("GranPro", "1500 hectáreas", "Funza", "gallinas, ovejas, toros")

print(granja1.nombre, granja1.tamaño, granja1.ubicacion, granja1.animales)
print(granja2.nombre, granja2.tamaño, granja2.ubicacion, granja2.animales)