# Ejercicio 3 — Cuenta de Banco Básica
class CuentaBanco:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Se depositaron {monto}. Saldo actual: {self.__saldo}")
        else:
            print("El monto debe ser mayor a 0.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Se retiraron {monto}. Saldo actual: {self.__saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")
        return self.__saldo

cuenta = CuentaBanco("Carlos", 100)
cuenta.consultar_saldo()
cuenta.depositar(50)
cuenta.retirar(30)
cuenta.retirar(200)
cuenta.consultar_saldo()
