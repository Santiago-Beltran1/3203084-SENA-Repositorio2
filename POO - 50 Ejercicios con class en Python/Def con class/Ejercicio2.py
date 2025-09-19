#Contar vocales de una frase que se ingrese

class ContadorVocales:
    def __init__(self, frase):
        self.frase = frase

    def contar(self):
        vocales = "aeiouAEIOU"
        return sum(1 for letra in self.frase if letra in vocales)

frase = input("Escribe una frase: ")
contador = ContadorVocales(frase)
print(f"La frase tiene {contador.contar()} vocal(es).")
