#Eliminador y actualizador de elementos en txt y con class

class ListaNombres:
    def __init__(self, archivo):
        self.archivo = archivo

    def agregar(self, nombre):
        with open(self.archivo, "a") as f:
            f.write(nombre + "\n")

    def mostrar(self):
        with open(self.archivo, "r") as f:
            print(f.read())

    def actualizar(self, viejo, nuevo):
        with open(self.archivo, "r") as f:
            lineas = f.readlines()
        with open(self.archivo, "w") as f:
            for l in lineas:
                f.write(nuevo + "\n" if l.strip() == viejo else l)

    def eliminar(self, nombre):
        with open(self.archivo, "r") as f:
            lineas = f.readlines()
        with open(self.archivo, "w") as f:
            for l in lineas:
                if l.strip() != nombre:
                    f.write(l)

lista = ListaNombres("nombres.txt")
lista.agregar("Santiago")
lista.agregar("Luz")
lista.mostrar()
lista.actualizar("Luz", "Carlos")
lista.eliminar("Santiago")
lista.mostrar()
