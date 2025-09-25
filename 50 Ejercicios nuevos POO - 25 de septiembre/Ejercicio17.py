# Ejercicio 17 — Empleado con Polimorfismo

class Empleado:
    def __init__(self, nombre, id_emp, salario_base):
        self.nombre = nombre
        self.id_emp = id_emp
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

class TiempoCompleto(Empleado):
    def __init__(self, nombre, id_emp, salario_base, beneficios):
        super().__init__(nombre, id_emp, salario_base)
        self.beneficios = beneficios

    def calcular_salario(self):
        return self.salario_base + self.beneficios

class TiempoParcial(Empleado):
    def __init__(self, nombre, id_emp, tarifa_hora, horas):
        super().__init__(nombre, id_emp, 0)
        self.tarifa_hora = tarifa_hora
        self.horas = horas

    def calcular_salario(self):
        return self.tarifa_hora * self.horas

emp1 = TiempoCompleto("Andres", 1, 1000, 200)
emp2 = TiempoParcial("Vinicius", 2, 20, 40)
print("Salario Tiempo Completo:", emp1.calcular_salario())
print("Salario Tiempo Parcial:", emp2.calcular_salario())
