#Clasificar edades 

class ClasificadorEdades:
    def __init__(self, cantidad):
        ninos = 0
        jovenes = 0
        adultos = 0

        for _ in range(cantidad):
            edad = int(input("Ingresa una edad: "))
            if edad <= 12:
                ninos += 1
            elif edad <= 17:
                jovenes += 1
            else:
                adultos += 1

        print(f"Niños: {ninos}, Jóvenes: {jovenes}, Adultos: {adultos}")

cantidad = int(input("¿Cuántas edades ingresará?: "))
clasificador = ClasificadorEdades(cantidad)
