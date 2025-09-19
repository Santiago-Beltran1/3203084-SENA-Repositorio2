#Promedio según notas en el diccionario

class notas:
    def __init__(self):
        self.calificaciones = {}

    def agregarN(self, estudiante, nota):
        if estudiante not in self.calificaciones:
            self.calificaciones[estudiante] = []
        self.calificaciones[estudiante].append(nota)

    def promedio(self, estudiante):
        if estudiante in self.calificaciones:
            notas = self.calificaciones[estudiante]
            promedio = sum(notas) / len(notas)
            print(f"Promedio de {estudiante}: {promedio:.2f}")
        else:
            print("Estudiante no encontrado.")

    def mostrar(self):
        print("Notas almacenadas:")
        for estudiante, notas in self.calificaciones.items():
            print(f"{estudiante}: {notas}")


reg = notas()
reg.agregarN("Luis", 4.5)
reg.agregarN("Luis", 3.8)
reg.agregarN("María", 5.0)
reg.promedio("Luis")
reg.mostrar()
