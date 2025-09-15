#Ejercicio 3
class empresa:
    def __init__(self, nombre, nTrabajadores, ubicacion, telefono):
        self.nombre = nombre
        self.nTrabajadores= nTrabajadores
        self.ubicacion = ubicacion
        self.telefono = telefono

empresa1 = empresa("Doria", "3000 Trabajadores", "cr10-282", "1111")
empresa2 = empresa("Purina", "3500 Trabajadores", "Calle 13", "2222")

print(empresa1.nombre, empresa1.nTrabajadores, empresa1.ubicacion, empresa1.telefono)
print(empresa2.nombre, empresa2.nTrabajadores, empresa2.ubicacion, empresa2.telefono)