#Conversor de temperatura

class Conversor:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo.lower()

    def convertir(self):
        if self.tipo == "c":
            return (self.valor * 9/5) + 32  
        elif self.tipo == "f":
            return (self.valor - 32) * 5/9 
        else:
            return None

valor = float(input("Ingrese la temperatura: "))
tipo = input("Escriba 'C' si es Celsius o 'F' si es Fahrenheit: ")
conv = Conversor(valor, tipo)
resultado = conv.convertir()

if resultado is not None:
    print(f"Temperatura convertida: {resultado:.2f}")
else:
    print("Tipo no válido.")
