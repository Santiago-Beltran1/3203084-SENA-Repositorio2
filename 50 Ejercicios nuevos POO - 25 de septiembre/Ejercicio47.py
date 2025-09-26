# Ejercicio 47 — Sistema de Logística

class Paquete:
    def __init__(self, id_pkg, peso, origen, destino):
        self.id_pkg = id_pkg
        self.peso = peso
        self.origen = origen
        self.destino = destino

class RutaLog:
    def __init__(self, id_ruta, paradas):
        self.id_ruta = id_ruta
        self.paradas = paradas

class AlmacenLog:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.inventario = []

pkg = Paquete(1, 10, "Bogotá", "Medellín")
ruta = RutaLog(1, ["Bogotá", "Honda", "Medellín"])
alm = AlmacenLog("Bodega Central")
alm.inventario.append(pkg)

print(pkg.destino)
print(alm.inventario)
print(ruta.paradas)
print(".Paquetes en almacén:", len(alm.inventario))
