#Crea un archivo con el texto y cuenta cuántas palabras ahí 

class contarPalabras:
    def __init__(self, archivo):
        self.archivo = archivo

    def guardar(self, texto):
        with open(self.archivo, "w") as f:
            f.write(texto)

    def contarP(self):
        try:
            with open(self.archivo, "r") as f:
                contenido = f.read()
                palabras = contenido.split()
                print(f"El archivo tiene {len(palabras)} palabras.")
        except FileNotFoundError:
            print("El archivo no existe.")

texto = input("Escriba un texto: ")
contador = contarPalabras("texto.txt")
contador.guardar(texto)
contador.contarP()
