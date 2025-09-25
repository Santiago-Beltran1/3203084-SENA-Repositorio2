# Ejercicio 19 — Sistema de Archivos

class ElementoSistema:
    def __init__(self, nombre):
        self.nombre = nombre

    def obtener_tamaño(self):
        raise NotImplementedError

class Archivo(ElementoSistema):
    def __init__(self, nombre, contenido=""):
        super().__init__(nombre)
        self.contenido = contenido

    def obtener_tamaño(self):
        return len(self.contenido)

class Carpeta(ElementoSistema):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.elementos = {}

    def agregar(self, e):
        self.elementos[e.nombre] = e

    def obtener_tamaño(self):
        return sum(e.obtener_tamaño() for e in self.elementos.values())

archivo1 = Archivo("notas.txt", "Servicio Nacional de Aprendizaje")
archivo2 = Archivo("data.txt", "Creador de documentos ejemplo")
carpeta = Carpeta("Documentos")
carpeta.agregar(archivo1)
carpeta.agregar(archivo2)
print("Tamaño total:", carpeta.obtener_tamaño())
