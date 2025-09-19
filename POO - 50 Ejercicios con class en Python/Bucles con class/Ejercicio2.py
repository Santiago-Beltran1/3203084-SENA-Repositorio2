#Cuenta de un número ingresado hasta llegar a 0

class cuenta:
    def __init__(self, inicio):
        self.inicio = inicio

    def regresar(self):
        print("\nProceso del número hasta llegar a 0:")
        while self.inicio >= 0:
            print(self.inicio)
            self.inicio -= 1
        print("Se a llegado a 0")

# Programa principal
inicio = int(input("Ingresa un número para la cuenta regresiva: "))
proceso = cuenta(inicio)
proceso.regresar()
