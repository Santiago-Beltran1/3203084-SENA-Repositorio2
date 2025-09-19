#Calcular Factorial

class Factorial:
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        factorial = 1
        for i in range(1, self.numero + 1):
            factorial *= i
        print(f"El factorial de {self.numero} es {factorial}")

num = int(input("Ingrese un número para calcular su factorial: "))
fact = Factorial(num)
fact.calcular()
