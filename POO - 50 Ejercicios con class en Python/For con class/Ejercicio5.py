#Calcular potencia para un número

class Potencias:
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        print(f"Potencias del {self.numero}:")
        for i in range(1, 6):
            print(f"{self.numero}^{i} = {self.numero ** i}")

num = int(input("Número para calcular potencias: "))
pot = Potencias(num)
pot.calcular()
