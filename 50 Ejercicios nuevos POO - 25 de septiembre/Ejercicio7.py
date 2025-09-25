# Ejercicio 7 — Contador de Palabras

class ContadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def contar_palabras(self):
        return len(self.texto.split())

    def contar_caracteres(self):
        return len(self.texto)

    def contar_lineas(self):
        return len(self.texto.splitlines())

texto = ContadorTexto("Servicio Nacional de Aprendizaje")
print("Palabras:", texto.contar_palabras())
print("Caracteres:", texto.contar_caracteres())
print("Líneas:", texto.contar_lineas())