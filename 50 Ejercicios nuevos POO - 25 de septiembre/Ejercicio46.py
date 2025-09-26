# Ejercicio 46 — Plataforma de Freelancing

class Freelancer:
    def __init__(self, id_freel, nombre):
        self.id_freel = id_freel
        self.nombre = nombre
        self.proyectos = []

class ProyectoFreel:
    def __init__(self, id_proj, titulo, cliente):
        self.id_proj = id_proj
        self.titulo = titulo
        self.cliente = cliente
        self.propuestas = []

class Propuesta:
    def __init__(self, freelancer, monto, descripcion):
        self.freelancer = freelancer
        self.monto = monto
        self.descripcion = descripcion

f = Freelancer(1, "Xiomara")
p = ProyectoFreel(1, "Diseño Web", "Empresa X")
pr = Propuesta(f, 500, "Diseño completo")
p.propuestas.append(pr)
print(f"Propuesta de {pr.freelancer.nombre} por {pr.monto}")
