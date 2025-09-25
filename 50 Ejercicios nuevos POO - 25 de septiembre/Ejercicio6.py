# Ejercicio 6 — Rectángulo Geométrico

class Rectangulo:
    def __init__(self, ancho_rect, alto_rect):
        self.ancho_rect = ancho_rect
        self.alto_rect = alto_rect

    def area(self):
        return self.ancho_rect * self.alto_rect

    def perimetro(self):
        return 2 * (self.ancho_rect + self.alto_rect)

    def es_cuadrado(self):
        return self.ancho_rect == self.alto_rect

r = Rectangulo(5, 10)
print("Área:", r.area())
print("Perímetro:", r.perimetro())
print("¿Es cuadrado?", r.es_cuadrado())
