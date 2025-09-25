# Ejercicio 36 — E-commerce

class Usuario:
    def __init__(self, id_usr, nombre):
        self.id_usr = id_usr
        self.nombre = nombre

class Producto:
    def __init__(self, id_prod, nombre, precio, stock):
        self.id_prod = id_prod
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Orden:
    def __init__(self, id_ord, usuario):
        self.id_ord = id_ord
        self.usuario = usuario
        self.items = []
        self.estado = "Creada"

    def agregar_item(self, producto, cant):
        if producto.stock >= cant:
            self.items.append((producto, cant))
            print(f"Agregado {cant} de {producto.nombre}.")
        else:
            print("Stock insuficiente.")

u = Usuario(1, "Torres")
p = Producto(1, "Celular", 500000, 10)
o = Orden(1, u)
o.agregar_item(p, 2)
