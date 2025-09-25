# Ejercicio 1 — Mi Primera Mascota

class Mascota:
    def __init__(self, mascota_nombre, especie, mascota_edad):
        self.mascota_nombre = mascota_nombre
        self.especie = especie
        self.mascota_edad = mascota_edad

    def presentarse(self):
        return f"Soy {self.mascota_nombre}, un(a) {self.especie}, tengo {self.mascota_edad} años"

m = Mascota("Luna", "gato", 3)
print(m.presentarse())
