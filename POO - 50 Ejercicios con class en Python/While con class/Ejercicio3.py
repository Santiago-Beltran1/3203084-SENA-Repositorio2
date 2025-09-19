#Calculadora de suma con todos los números ingresados

class suma:
    def __init__(self):
        self.total = 0

    def sumar(self):
        numero = None
        while numero != 0:
            numero = int(input("Ingrese un número (o ponga 0 para terminar): "))
            self.total += numero
        print(f"Suma total: {self.total}")

suma = suma()
suma.sumar()
