# 29. Sistema de Reservas

class Reserva:
    def __init__(self, usuario, recurso, inicio, fin):
        self.usuario = usuario
        self.recurso = recurso
        self.inicio = inicio
        self.fin = fin

    def __str__(self):
        return f"{self.usuario} reservó {self.recurso} de {self.inicio} a {self.fin}"

class SistemaReservas:
    def __init__(self):
        self.reservas = []

    def crear_reserva(self, usuario, recurso, inicio, fin):
        for r in self.reservas:
            if r.recurso == recurso and not (fin <= r.inicio or inicio >= r.fin):
                print("Conflicto de horarios")
                return
        self.reservas.append(Reserva(usuario, recurso, inicio, fin))
        print("Reserva creada con éxito")

    def ver_reservas(self):
        for r in self.reservas:
            print(r)

sistema = SistemaReservas()

while True:
    print("\n1. Crear reserva\n2. Ver reservas\n3. Salir")
    op = input("Opción: ")
    if op == "1":
        usuario = input("Usuario: ")
        recurso = input("Recurso: ")
        inicio = int(input("Hora inicio: "))
        fin = int(input("Hora fin: "))
        sistema.crear_reserva(usuario, recurso, inicio, fin)
    elif op == "2":
        sistema.ver_reservas()
    elif op == "3":
        break
    else:
        print("Opción inválida")
