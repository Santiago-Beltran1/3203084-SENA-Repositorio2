# Ejercicio 32 — Clínica Médica

class Paciente:
    def __init__(self, cedula, nombre, edad):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.historial = []

class Doctor:
    def __init__(self, cedula, nombre, especialidad):
        self.cedula = cedula
        self.nombre = nombre
        self.especialidad = especialidad
        self.citas = []

class Cita:
    contador = 1
    def __init__(self, paciente, doctor, fecha):
        self.id = Cita.contador
        Cita.contador += 1
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.estado = "Programada"

pac = Paciente("789", "Laura García", 27)
doc = Doctor("101", "Dr. Martín Pérez", "Dermatología")

cita = Cita(pac, doc, "2025-10-15")

print(f"Cita {cita.id}: Paciente {cita.paciente.nombre} con {cita.doctor.nombre} el {cita.fecha}")
