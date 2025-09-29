# Ejercicio 1 — Mi Primera Mascota

class Mascota:
    def __init__(self, mascota_nombre, especie, mascota_edad):
        self.mascota_nombre = mascota_nombre
        self.especie = especie
        self.mascota_edad = mascota_edad

    def presentarse(self):
        print(f"nombre de la mascota: {self.mascota_nombre}, especie: {self.especie}, edad: {self.mascota_edad} años")

animal1 = Mascota("Lira", "loro", 3)
animal2 = Mascota("Ragnarok", "caballo", 10)
print(animal1.presentarse())
