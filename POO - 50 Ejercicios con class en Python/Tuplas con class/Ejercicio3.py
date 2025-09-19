#Simulación de un tiquete de viaje

class viaje:
    def __init__(self):
        self.lugares = (("Cartagena", 500000), ("Villao", 100000), ("Medellín", 300000))

    def mostrar_destinos(self):
        print("\nDestinos disponibles:")
        for i, (lugar, precio) in enumerate(self.lugares, start=1):
            print(f"{i}. {lugar} - ${precio}")

    def elegir_destino(self, opcion):
        if 1 <= opcion <= len(self.lugares):
            lugar, precio = self.lugares[opcion - 1]
            print(f"Has elegido viajar a {lugar} con valor de ${precio}")
        else:
            print("Opción no válida.")


v = viaje()
v.mostrar_destinos()
opcion = int(input("Elige un destino (1-3): "))
v.elegir_destino(opcion)
