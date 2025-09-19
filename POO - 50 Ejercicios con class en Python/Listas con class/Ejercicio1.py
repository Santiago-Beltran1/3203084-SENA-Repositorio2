#Agregador de indices a una lista

class Lista:
    def __init__(self): self.datos = []

    def agregar(self, x): self.datos.append(x)

lista = Lista()
while True:
    x = input("Ingresa un valor (o 'salir'): ")
    if x == "salir":
        break
    lista.agregar(x)

print("Lista final:", lista.datos)