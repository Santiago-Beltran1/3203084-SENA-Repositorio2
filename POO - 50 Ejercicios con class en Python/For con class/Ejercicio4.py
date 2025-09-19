#Cuenta vocales

class ContadorVocales:
    def __init__(self, palabra):
        self.palabra = palabra.lower()

    def contarVocal(self):
        contador = 0
        for letra in self.palabra:
            if letra in "aeiou":
                contador += 1
        print(f"La palabra tiene {contador} vocal(es).")

palabra = input("Ingresa una palabra: ")
contador = ContadorVocales(palabra)
contador.contarVocal()
