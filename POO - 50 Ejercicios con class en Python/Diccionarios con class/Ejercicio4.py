#Sistema de precios y actualizaciones

class SistemaPrecios:
    def __init__(self):
        self.precios = {}

    def agregarProd(self, producto, precio):
        self.precios[producto] = precio

    def actuPrecio(self, producto, nuevo_precio):
        if producto in self.precios:
            self.precios[producto] = nuevo_precio
            print(f"Precio de {producto} actualizado a ${nuevo_precio}")
        else:
            print("Producto no encontrado.")

    def mostrar(self):
        print("Lista de precios:")
        for producto, precio in self.precios.items():
            print(f"{producto}: ${precio}")


sp = SistemaPrecios()
sp.agregarProd("Gaseosa", 5000)
sp.agregarProd("galletas", 1500)
sp.actuPrecio("Gaseosa", 6000)
sp.mostrar()
