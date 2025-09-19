#Encuesta sobre alguna pregunta

class EncuestaPreg:
    def __init__(self):
        self.respuestas = []

    def realizar_encuesta(self):
        print("Responda 'si' o 'no' a la siguiente pregunta (escriba 'fin' para finalizar el proceso):")
        pregunta = ""
        while pregunta.lower() != "fin":
            pregunta = input("¿Te gusta la programación? (si/no o 'fin'): ")
            if pregunta.lower() in ["si", "no"]:
                self.respuestas.append(pregunta)

        print(f"\nResultado Votación: {self.respuestas.count('si')} sí, {self.respuestas.count('no')} no")

encuesta = EncuestaPreg()
encuesta.realizar_encuesta()
