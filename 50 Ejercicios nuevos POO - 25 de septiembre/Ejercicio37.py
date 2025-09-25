# Ejercicio 37 — Sistema de Gestión Hotelera

class Habitacion:
    def __init__(self, num, tipo, precio):
        self.num = num
        self.tipo = tipo
        self.precio = precio
        self.reservas = []

class Reserva:
    def __init__(self, habitacion, fecha_inicio, fecha_fin, huesped):
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.huesped = huesped

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = {}

    def agregar_habitacion(self, hab):
        self.habitaciones[hab.num] = hab

h = Hotel("Los Castillos")
hab = Habitacion(510, "Suite", 200)
h.agregar_habitacion(hab)
print("Habitaciones del hotel:", list(h.habitaciones.keys()))
