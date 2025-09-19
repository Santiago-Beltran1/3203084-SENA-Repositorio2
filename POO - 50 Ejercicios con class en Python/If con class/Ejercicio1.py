#Detector de edad 

class Evento:
    def __init__(self, edad):
        self.edad = edad

    def verificar(self):
        if self.edad >= 18:
            print("Puede entrar al evento.")
        else:
            print("No puede entrar, debe tener al menos 18 años.")

edad = int(input("Ingrese su edad: "))
evento = Evento(edad)
evento.verificar()
