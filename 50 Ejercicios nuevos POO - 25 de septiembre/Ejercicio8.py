# Ejercicio 8 — Producto de Tienda

class ProductoTienda:
    def __init__(self, codigo, nombre_prod, precio, stock):
        self.codigo = codigo
        self.nombre_prod = nombre_prod
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            self.precio *= (1 - porcentaje / 100)
            print(f"Descuento aplicado. Nuevo precio: {self.precio}")

    def hay_stock(self, cantidad):
        return self.stock >= cantidad

prod = ProductoTienda(101, "Camiseta", 50, 20)
prod.aplicar_descuento(10)
print("¿Hay stock de 5?", prod.hay_stock(5))