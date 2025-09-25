# Ejercicio 25 — Inventario de Tienda

class ProductoInv:
    def __init__(self, codigo, nombre, precio, stock_min=10):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = 0
        self.stock_min = stock_min

    def agregar_stock(self, cant):
        self.stock += cant
        print(f"Se agregaron {cant} unidades. Stock actual: {self.stock}")

    def reducir_stock(self, cant):
        if 0 < cant <= self.stock:
            self.stock -= cant
            print(f"Se redujeron {cant} unidades. Stock actual: {self.stock}")
        else:
            print("No hay suficiente stock.")

    def necesita_reposicion(self):
        return self.stock <= self.stock_min

prod = ProductoInv(101, "Teclado", 50)
prod.agregar_stock(5)
prod.reducir_stock(3)
print("¿Necesita reposición?", prod.necesita_reposicion())
