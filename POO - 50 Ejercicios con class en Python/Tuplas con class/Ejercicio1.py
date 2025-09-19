#Carta y precio del pedido que se haga

class Carta:
    def __init__(self):
        self.menu = (("bandeja paisa", 25000), ("ajiaco", 20000), ("salchipapa", 12000))

    def mostrar_menu(self):
        print("\nMenú:")
        for i, (plato, precio) in enumerate(self.menu, start=1):
            print(f"{i}. {plato} - ${precio}")

    def pedir_plato(self, opcion):
        if 1 <= opcion <= len(self.menu):
            plato, precio = self.menu[opcion - 1]
            print(f"Usted pidió: {plato} - Con valor de: ${precio}")
        else:
            print("Opción no válida.")


rest = Carta()
rest.mostrar_menu()
opcion = int(input("Elija un plato (1-3): "))
rest.pedir_plato(opcion)
