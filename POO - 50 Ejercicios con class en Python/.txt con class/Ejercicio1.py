#Guardar nombres con class y en archivo txt

class AprendicesTXT:
    def __init__(self, archivo):
        self.archivo = archivo

    def guardar(self, nombre):
        with open(self.archivo, "a") as f:
            f.write(nombre + "\n")

archivo = "aprendices.txt"
app = AprendicesTXT(archivo)

for _ in range(3):
    nombre = input("Nombre aprendiz: ")
    app.guardar(nombre)

print("Aprendices guardados en", archivo)
