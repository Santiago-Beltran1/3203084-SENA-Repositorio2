# Ejercicio 45 — Sistema de Gestión Hospitalaria

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []

class Tratamiento:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

dep1 = Departamento("Dermatología")
t1 = Tratamiento("Tratamieto de piel", "Injerción de piel")
dep1.doctores.append("Dr. Tavárez")
dep1 = Departamento("Dermatología")
t1 = Tratamiento("Monitoreo de manchas y anomalias", "-Por revisar")
dep1.doctores.append("Dr. Enrique")


dep2 = Departamento("Odontología")
t2 = Tratamiento("Ondodoncia", "Sacar resto de una muela")
dep2.doctores.append("Dr. Muelitas")
dep2 = Departamento("Odontología")
t2 = Tratamiento("Eliminación de caries", "Puesta de una calsa")
dep2.doctores.append("Dr. Ricky")

print(f"Departamento: {dep1.nombre}, Doctores: {dep1.doctores} Tratamientos: {t1.descripcion}")
print(f"Departamento: {dep2.nombre}, Doctores: {dep2.doctores} Tratamientos: {t2.descripcion}")
