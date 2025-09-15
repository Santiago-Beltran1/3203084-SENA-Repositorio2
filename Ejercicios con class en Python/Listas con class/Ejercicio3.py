class ListaBusqueda:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def buscar(self, elemento):
        return elemento in self.elementos

# Uso
lista = ListaBusqueda()
lista.agregar("hola")
print(lista.buscar("hola"))  # True
print(lista.buscar("adios"))  # False