#Ingresar elementos y eliminarlos 

class eliminar:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)

    def mostrar(self):
        return self.elementos

lista = eliminar()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.eliminar(1)
print(lista.mostrar()) 