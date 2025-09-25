# Ejercicio 41 — Sistema Bancario Completo

class Cuenta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo

    def depositar(self, monto):
        self._saldo += monto
        print(f"Depósito de {monto}. Saldo actual: {self._saldo}")

    def retirar(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
            print(f"Retiro de {monto}. Saldo actual: {self._saldo}")
        else:
            print("Fondos insuficientes.")

    def saldo(self):
        return self._saldo

c = Cuenta("1", "Ana", 500)
c.depositar(200)
c.retirar(100)
print("Saldo final:", c.saldo())
