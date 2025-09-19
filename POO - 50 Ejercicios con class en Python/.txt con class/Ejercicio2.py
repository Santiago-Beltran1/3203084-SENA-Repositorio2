#Lee los archivos que ahí en un archivo que ya creamos .txt

class LeerArchivo:
    def __init__(self, archivo):
        self.archivo = archivo

    def mostrar(self):
        with open(self.archivo, "r") as f:
            print(f.read())

lector = LeerArchivo("aprendices.txt")
lector.mostrar()
