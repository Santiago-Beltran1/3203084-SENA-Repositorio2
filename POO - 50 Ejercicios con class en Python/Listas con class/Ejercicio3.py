#Mirar si hay un elemento en la lista con class

class Buscar:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def buscar(self, elemento):
        return elemento in self.elementos

lista = Buscar()
lista.agregar("Real Madrid")
print(lista.buscar("Real Madrid"))  
print(lista.buscar("Bayern Munich"))  