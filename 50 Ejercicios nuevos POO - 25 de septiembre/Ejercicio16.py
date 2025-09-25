# Ejercicio 16 — Vehículo con Herencia

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} encendido.")

    def apagar(self):
        self.encendido = False
        print(f"{self.marca} {self.modelo} apagado.")

class Carro(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

class Bicicleta(Vehiculo):
    def __init__(self, marca, tipo):
        super().__init__(marca, "bicicleta")
        self.tipo = tipo

carro = Carro("Toyota", "Corolla", 4)
carro.encender()
carro.apagar()

bici = Bicicleta("Trek", "Montaña")
bici.encender()
