#Planeador de que deberá cocinar un día en especifico

class PlanComidas:
    def __init__(self):
        self.platos = (
            ("Arroz con pollo", "Almuerzo"), ("Ensalada", "Cena"), ("Arepas", "Desayuno"), ("Sancocho", "Almuerzo"), ("Pasta", "Cena"))

    def planificar(self):
        dias = int(input("Ingrese el número de días para ver que tendrá que cocinar ese día: "))
        print("\nPlan de comidas:")
        index = 0
        for dia in range(1, dias + 1):
            plato = self.platos[index % len(self.platos)] 
            print(f"Día {dia}: {plato[0]} ({plato[1]})")
            index += 1

comidas = PlanComidas()
comidas.planificar()
