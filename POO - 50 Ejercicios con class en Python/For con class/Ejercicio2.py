#Listador de productos

class Productos:
    def __init__(self):
        self.productos = []

    def agregarProd(self):
        cantidad = int(input("¿Cuántos productos desea ingresar? "))
        for _ in range(cantidad):
            producto = input("Nombre del producto: ")
            self.productos.append(producto)

    def mostrarProd(self):
        print("\nLista de productos:")
        for i, prod in enumerate(self.productos, 1):
            print(f"{i}. {prod}")

lista = Productos()
lista.agregarProd()
lista.mostrarProd()
