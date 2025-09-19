#Probador de si una contraseña es correcta

class contra:
    def __init__(self, contraCorrecta):
        self.contraCorrecta = contraCorrecta

    def adivinar(self):
        intento = ""
        while intento != self.contraCorrecta:
            intento = input("Adivina la contraseña: ")
            if intento == self.contraCorrecta:
                print("¡Contraseña correcta!")
            else:
                print("Contraseña incorrecta, intente otra vez.")

contra = contra("sena2025")
contra.adivinar()
