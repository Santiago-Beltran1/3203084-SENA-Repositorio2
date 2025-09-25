# Ejercicio 4 — Lista de Tareas

class TareaItem:
    def __init__(self, id_item, texto):
        self.id_item = id_item
        self.texto = texto
        self.completada = False

class ListaTareas:
    def __init__(self):
        self._tareas = {}

    def agregar(self, id_item, texto):
        self._tareas[id_item] = TareaItem(id_item, texto)
        print(f"Tarea '{texto}' agregada.")

    def eliminar(self, id_item):
        if id_item in self._tareas:
            del self._tareas[id_item]
            print(f"Tarea {id_item} eliminada.")
        else:
            print("Tarea no encontrada.")

    def marcar_completada(self, id_item):
        if id_item in self._tareas:
            self._tareas[id_item].completada = True
            print(f"Tarea {id_item} marcada como completada.")

    def mostrar(self):
        for t in self._tareas.values():
            estado = "Completada" if t.completada else "Pendiente"
            print(f"[{t.id_item}] {t.texto} - {estado}")

lista = ListaTareas()
lista.agregar(1, "Estudiar POO")
lista.agregar(2, "Hacer ejercicio")
lista.agregar(3, "Tender la cama")
lista.agregar(4, "Dormir")
lista.marcar_completada(1)
lista.marcar_completada(2)
lista.mostrar()