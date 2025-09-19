#Imprime el horario con materia y hora

class Horarios:
    def __init__(self):
        self.horarios = (("Inglés", "7:00 AM"), ("Back-end", "10:00 AM"), ("Front-end", "2:00 PM"))

    def mostrar_horarios(self):
        print("\nHorario en todo el día:")
        for materia, hora in self.horarios:
            print(f"{materia}: {hora}")


h = Horarios()
h.mostrar_horarios()
