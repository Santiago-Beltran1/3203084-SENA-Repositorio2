#Sistema asistencia

class Asistencia:
    def __init__(self):
        self.presentes = []

    def marcar(self, nombre):
        if input(f"¿{nombre} está? (s/n): ") == "s":
            self.presentes.append(nombre)

    def mostrar(self):
        print("Presentes:", ", ".join(self.presentes))

a = Asistencia()
for n in ["Ana", "Luis", "Carlos"]:
    a.marcar(n)
a.mostrar()
