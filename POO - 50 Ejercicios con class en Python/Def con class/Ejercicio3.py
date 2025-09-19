#Lista de compras según los que se ingrese

class ListaCompras:
    def __init__(self):
        self.compras = []

    def agregar_producto(self, producto):
        self.compras.append(producto)

    def mostrar_lista(self):
        print("Su lista de compras es:")
        for i, p in enumerate(self.compras, start=1):
            print(f"{i}. {p}")

lista = ListaCompras()
print("Agrege productos a la lista (escriba 'fin' para finalizar el proceso):")
while True:
    producto = input("Producto: ")
    if producto.lower() == "fin":
        break
    lista.agregar_producto(producto)

lista.mostrar_lista()
