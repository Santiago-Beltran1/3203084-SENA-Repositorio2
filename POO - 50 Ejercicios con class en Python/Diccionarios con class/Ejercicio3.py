#Priorizador de tareas

class priorizar:
    def __init__(self):
        self.tareas = {}

    def agregTarea(self, tarea, prioridad):
        self.tareas[tarea] = prioridad

    def mostrar(self):
        print("Tareas ordenadas por prioridad:")
        for tarea, prioridad in sorted(self.tareas.items(), key=lambda x: x[1]):
            print(f"{tarea} (Prioridad: {prioridad})")


gt = priorizar()
gt.agregTarea("Ir al gimnasio", 2)
gt.agregTarea("Hacer trabajos", 1)
gt.agregTarea("Dormir", 3)
gt.mostrar()
