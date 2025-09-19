#Tabla de multiplicar

class Tabla:
    def __init__(self, numero):
        self.numero = numero

    def creador(self):
        print(f"\nTabla del {self.numero}:")
        for i in range(1, 11):
            print(f"{self.numero} x {i} = {self.numero * i}")

num = int(input("Ingresa un número: "))
tabla = Tabla(num)
tabla.creador()
