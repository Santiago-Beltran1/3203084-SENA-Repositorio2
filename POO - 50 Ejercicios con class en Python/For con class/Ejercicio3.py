#Secuencia para llegar a un número

class Secuencia:
    def __init__(self, limite):
        self.limite = limite

    def generar(self):
        print(f"Secuencia hasta {self.limite}:")
        for i in range(1, self.limite + 1):
            print(i, end=" ")

limite = int(input("Ingrese un número límite: "))
serie = Secuencia(limite)
serie.generar()
