#Imprimidor de inventario

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregarPro(self, nombre, cantidad):
        self.productos[nombre] = cantidad

    def vender(self, nombre, cantidad):
        if nombre in self.productos and self.productos[nombre] >= cantidad:
            self.productos[nombre] -= cantidad
            print(f"Venta realizada: {cantidad} de {nombre}")
        else:
            print("No hay suficiente stock o producto no existe.")

    def mostrar(self):
        print("Inventario actual:")
        for producto, cantidad in self.productos.items():
            print(f"{producto}: {cantidad} unidades")


inv = Inventario()
inv.agregarPro("Manzanas", 10)
inv.agregarPro("Pan", 5)
inv.vender("Manzanas", 3)
inv.mostrar()
