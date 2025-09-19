#Descuento según si tiene tarjeta

class Tienda:
    def __init__(self, precio, tarjeta):
        self.precio = precio
        self.tarjeta = tarjeta

    def calcular_descuento(self):
        if self.tarjeta.lower() == "si":
            print(f"Precio con descuento: {self.precio * 0.8} COP")
        else:
            print(f"Precio sin descuento: {self.precio} COP")

precio = float(input("Ingrese el precio del producto: "))
tarjeta = input("¿Tiene tarjeta de descuento? (si/no): ")
tienda = Tienda(precio, tarjeta)
tienda.calcular_descuento()
