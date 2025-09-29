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

    def mostrar(self):
        if not self._contactos:
            print("No hay contactos en la agenda.")
        else:
            print("Contactos en la agenda:")
            for id_contacto, contacto in self._contactos.items():
                print(f"{id_contacto}: {contacto.nombre} - {contacto.telefono} - {contacto.email}")

agenda = Agenda()
agenda.agregar(1, Contacto("Ricardo", "00000", "ricardo@gmail.com"))
agenda.agregar(2, Contacto("Linda", "11111", "linda@gmail.com"))
agenda.buscar_por_nombre("Linda")
agenda.buscar_por_nombre("Linda")

print("\n--- Todos los contactos ---")
agenda.mostrar()