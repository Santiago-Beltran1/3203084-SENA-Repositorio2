#Simular un pago de productos

class RegProcuct:
    def __init__(self):
        total = 0
        precio = -1

        while precio != 0:
            precio = float(input("Precio del producto (0 para terminar): "))
            if precio != 0:
                total += precio

        if total > 0:
            print(f"Total a pagar: ${total}")
        else:
            print("No se compraron productos.")

caja = RegProcuct()
