# Ejercicio 10 — Agenda de Contactos

class Contacto:
    def __init__(self, nombre, telefono, email=""):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self._contactos = {}

    def agregar(self, id_contacto, contacto):
        self._contactos[id_contacto] = contacto
        print(f"Contacto {contacto.nombre} agregado.")

    def buscar_por_nombre(self, nombre):
        resultados = [c for c in self._contactos.values() if nombre.lower() in c.nombre.lower()]
        for c in resultados:
            print(f"{c.nombre} - {c.telefono}")

agenda = Agenda()
agenda.agregar(1, Contacto("Ricardo", "00000"))
agenda.agregar(2, Contacto("Linda", "11111"))
agenda.buscar_por_nombre("Linda")
