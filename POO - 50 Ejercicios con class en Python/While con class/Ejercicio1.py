#Ejercicio de un contador que va ascendiendo hasta que el número que diga el usuario

class cuentaArriba:
    def __init__(self, limite):
        self.limite = limite

    def contar(self):
        i = 1
        while i <= self.limite:
            print(i, end=" ")
            i += 1

limite = int(input("Contar hasta: "))
contador = cuentaArriba(limite)
contador.contar()
