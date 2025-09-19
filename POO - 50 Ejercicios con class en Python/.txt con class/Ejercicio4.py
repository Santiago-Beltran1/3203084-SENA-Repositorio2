#Crea el archivo txt con las notas y muestra el promedio

class PromedioNotas:
    def __init__(self, archivo):
        self.archivo = archivo

    def guardar(self, nota):
        with open(self.archivo, "a") as f:
            f.write(str(nota) + "\n")

    def promedio(self):
        try:
            with open(self.archivo, "r") as f:
                notas = [float(n) for n in f.readlines()]
                if notas:
                    print(f"Promedio: {sum(notas)/len(notas):.2f}")
                else:
                    print("No hay notas registradas.")
        except FileNotFoundError:
            print("Archivo no encontrado.")

p = PromedioNotas("notas.txt")
p.guardar(4.0)
p.guardar(4.5)
p.promedio()
