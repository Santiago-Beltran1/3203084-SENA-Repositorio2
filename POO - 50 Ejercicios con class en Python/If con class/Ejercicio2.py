#Mensaje según el clima que se ponga

class Clima:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def clasificar(self):
        if self.temperatura < 15:
            print("Mucho frío")
        elif 15 <= self.temperatura <= 25:
            print("Clima templado")
        else:
            print("Mucha calor")

temp = float(input("Ingrese la temperatura en grados centígrados: "))
clima = Clima(temp)
clima.clasificar()
