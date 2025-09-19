#Encuesta abierta sobre peliculas

class EncuestaPeliculas:
    def __init__(self):
        self.votos = {}

    def votar(self):
        print("Vote por su película favorita (escriba 'fin' para finalizar el proceso):")
        pelicula = ""
        while pelicula.lower() != "fin":
            pelicula = input("Película: ")
            if pelicula.lower() != "fin":
                if pelicula in self.votos:
                    self.votos[pelicula] += 1
                else:
                    self.votos[pelicula] = 1

        print("\nResultados de la votación:")
        for peli, votos in self.votos.items():
            print(f"{peli}: {votos} votos")

encuesta = EncuestaPeliculas()
encuesta.votar()
