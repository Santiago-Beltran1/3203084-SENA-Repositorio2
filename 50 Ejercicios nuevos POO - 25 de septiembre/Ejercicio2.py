# Ejercicio 2 — Calculadora Simple

class CalculadoraSimple:
    def sumar(self, a_sum, b_sum): 
        return a_sum + b_sum
    def restar(self, a_res, b_res): 
        return a_res - b_res
    def multiplicar(self, a_mul, b_mul): 
        return a_mul * b_mul
    def dividir(self, a_div, b_div):
        if b_div == 0: 
            return "Error: División por cero"
        return a_div / b_div

calc = CalculadoraSimple()
print("Suma:", calc.sumar(10, 5))
print("Resta:", calc.restar(10, 5))
print("Multiplicación:", calc.multiplicar(10, 5))
print("División:", calc.dividir(10, 0))
print("División válida:", calc.dividir(10, 5))
