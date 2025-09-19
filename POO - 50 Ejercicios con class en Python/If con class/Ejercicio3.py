#Mostrar si se obtiene o no una beca

class Beca:
    def __init__(self, nota, asistencia):
        self.nota = nota
        self.asistencia = asistencia

    def evaluar(self):
        if self.nota >= 4.0 and self.asistencia >= 80:
            print("Consigue la beca.")
        elif self.nota >= 4.0:
            print("Mejore la asistencia para la beca.")
        else:
            print("No cumple con los requisitos.")

nota = float(input("Ingrese su nota promedio: "))
asistencia = int(input("Ingrese su porcentaje de asistencia (del 0 al 100): "))
beca = Beca(nota, asistencia)
beca.evaluar()
