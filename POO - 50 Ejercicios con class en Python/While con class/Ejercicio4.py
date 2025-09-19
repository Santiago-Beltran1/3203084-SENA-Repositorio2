#Menú usando while

class Menu:
    def mostrar(self):
        opcion = ""
        while opcion != "3":
            print("\n--- Menú ---")
            print("1. Saludar")
            print("2. Despedirse")
            print("3. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                print("Hola, Bienvenido al SENA")
            elif opcion == "2":
                print("Nos vemos")
            elif opcion != "3":
                print("Opción no válida")

menu = Menu()
menu.mostrar()
