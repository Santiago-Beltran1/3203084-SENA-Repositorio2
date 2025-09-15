class Producto:
    print("Esta clase es nueva")

    def __init__(self, producto, precio):
        self.precio = precio
        self.producto = producto

    def __str__(self):
        return f"{self.producto}, {self.precio}"

    def __repr__(self):
        return f"{self.producto}, {self.precio}"

    def __format__(self, formato):
        if formato == "precio":
            return f"{self.precio}"
        return str(self)

var = Producto("computador", 3000000)

print(var)             
print(repr(var))       
print(f"{var.precio}") 