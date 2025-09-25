# Ejercicio 35 — Sistema de Votación

class Votante:
    def __init__(self, id_vot, nombre):
        self.id_vot = id_vot
        self.nombre = nombre

class Eleccion:
    def __init__(self, nombre, candidatos):
        self.nombre = nombre
        self.candidatos = {c: 0 for c in candidatos}
        self.votantes = set()

    def votar(self, votante, candidato):
        if votante.id_vot not in self.votantes and candidato in self.candidatos:
            self.candidatos[candidato] += 1
            self.votantes.add(votante.id_vot)
            print(f"{votante.nombre} votó por {candidato}.")
        else:
            print("Voto inválido o repetido.")

    def resultados(self):
        return self.candidatos

e = Eleccion("Presidencial", ["Petro", "Pastrana"])
v1 = Votante(1, "Johan")
v2 = Votante(2, "Mariana")
e.votar(v1, "Petro")
e.votar(v2, "Pastrana")
print("Resultados:", e.resultados())
