#Imprimir la canción con su autor 

class Repertorio:
    def __init__(self):
        self.canciones = ()

    def agregar_cancion(self, titulo, artista):
        self.canciones += ((titulo, artista),)

    def mostrar_canciones(self):
        print("\nRepertorio de canciones:")
        for titulo, artista in self.canciones:
            print(f"{titulo} - {artista}")


cf = Repertorio()
cf.agregar_cancion("Olimpo", "Milo J.")
cf.agregar_cancion("Hace Tiempo", "Blessd")
cf.mostrar_canciones()
