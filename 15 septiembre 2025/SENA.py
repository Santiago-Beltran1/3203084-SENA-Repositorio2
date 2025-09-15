#Ejercicio 5
class SENA:
    def __init__(self, sede, programa, ficha, jornada):
        self.sede= sede
        self.programa = programa 
        self.ficha = ficha
        self.jornada = jornada

SENA1 = SENA("CBA Mosquera", "ADSO", "3203084", "diurna")
SENA2 = SENA("Madrid", "Cocina", "2983832", "mixta")

print(SENA1.sede, SENA1.programa, SENA1.ficha, SENA1.jornada)
print(SENA2.sede, SENA2.programa, SENA2.ficha, SENA2.jornada)