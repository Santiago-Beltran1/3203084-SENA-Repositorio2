#Promedio de notas ingresadas por usuario más su resultado

class CalculadoraNotas:
    def __init__(self, total_notas):
        suma = 0
        for _ in range(total_notas):
            nota = float(input("Ingresa la nota: "))
            suma += nota
        
        promedio = suma / total_notas
        if promedio >= 3:
            print(f"Promedio: {promedio:.2f} → Aprobado")
        else:
            print(f"Promedio: {promedio:.2f} → Reprobado")

notas = int(input("¿Cuántas notas ingresarás?: "))
calc = CalculadoraNotas(notas)
