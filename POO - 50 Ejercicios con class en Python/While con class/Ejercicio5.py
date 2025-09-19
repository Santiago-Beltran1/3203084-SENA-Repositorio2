#Contador de vocales en todas las palabras que se ingresen

class cVocales:
    def __init__(self):
        self.totalVocales = 0

    def contar(self):
        palabra = ""
        while palabra.lower() != "fin":
            palabra = input("Ingresa una palabra (o ingrese'fin' para finalizar el proceso): ")
            if palabra.lower() != "fin":
                for letra in palabra.lower():
                    if letra in "aeiou":
                        self.totalVocales += 1
        print(f"Total de vocales ingresadas: {self.totalVocales}")

contador = cVocales()
contador.contar()
