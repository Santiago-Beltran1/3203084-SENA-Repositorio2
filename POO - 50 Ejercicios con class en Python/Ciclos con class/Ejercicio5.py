#Sistema de acceso

class acceder:
    def __init__(self, codigo_correcto, intentos):
        i = 0
        acceso = False
        while i < intentos:
            codigo = input("Ingresa el código de acceso: ")
            if codigo == codigo_correcto:
                print("Código correcto, puede entrar")
                acceso = True
                break
            else:
                print("Código incorrecto, no puede entrar")
            i += 1

        if not acceso:
            print("Se acabaron los intentos.")

control = acceder("SENITA", 3)
