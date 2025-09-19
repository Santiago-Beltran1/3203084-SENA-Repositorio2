#Máximo de un número de los que se pongan

class ListaMaximo:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def maximo(self):
        if self.elementos:
            return max(self.elementos)
        return None

# Uso
lista = ListaMaximo()
lista.agregar(4)
lista.agregar(9)
print("el número más grande es: ", lista.maximo()) 