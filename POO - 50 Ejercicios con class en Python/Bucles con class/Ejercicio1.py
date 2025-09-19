#Tabla de el cuadrado de un número según los limites que se establezcan

class Cuadrados:
    def __init__(self, limite):
        self.limite = limite

    def mostrarC(self):
        print(f"\nCuadrados del 1 al {self.limite}:")
        for i in range(1, self.limite + 1):
            print(f"{i}² = {i * i}")

limite = int(input("Ingresa un número límite: "))
cuad = Cuadrados(limite)
cuad.mostrarC()
