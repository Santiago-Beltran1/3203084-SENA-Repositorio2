# 24. Cuenta Bancaria

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de {monto}. Saldo actual: {self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto}. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes")

cuenta = CuentaBancaria("Juan", 1000)

while True:
    print("\n1. Depositar\n2. Retirar\n3. Ver saldo\n4. Salir")
    op = input("Opción: ")
    if op == "1":
        monto = float(input("Monto: "))
        cuenta.depositar(monto)
    elif op == "2":
        monto = float(input("Monto: "))
        cuenta.retirar(monto)
    elif op == "3":
        print("Saldo actual:", cuenta.saldo)
    elif op == "4":
        break
    else:
        print("Opción inválida")
