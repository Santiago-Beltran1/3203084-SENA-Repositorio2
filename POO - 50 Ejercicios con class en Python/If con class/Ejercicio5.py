#Verificador de capacidad en una sala de evento

class Sala:
    def __init__(self, maximo, actuales):
        self.maximo = maximo
        self.actuales = actuales

    def verificar(self):
        if self.actuales < self.maximo:
            print("Hay espacio disponible en la sala.")
        else:
            print("Sala llena, no se puede ingresar.")

maximo = int(input("Capacidad máxima: "))
actuales = int(input("Personas actuales: "))
sala = Sala(maximo, actuales)
sala.verificar()
