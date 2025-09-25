# Ejercicio 20 — Instrumentos Musicales

class Instrumento:
    def tocar(self):
        raise NotImplementedError

class Guitarra(Instrumento):
    def tocar(self):
        return "Suena una guitarra"

class Piano(Instrumento):
    def tocar(self):
        return "Suena un piano"

g = Guitarra()
p = Piano()
print(g.tocar())
print(p.tocar())
