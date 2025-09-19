#Contador de impares

class contadorN:
    def __init__(self, limite):
        self.limite = limite
        pares = 0
        impares = 0

        for i in range(1, self.limite + 1):
            if i % 2 == 0:
                pares += 1
            else:
                impares += 1

        print(f"Pares: {pares}, Impares: {impares}")

limite = int(input("Ingresa el número límite: "))
contador = contadorN(limite)
