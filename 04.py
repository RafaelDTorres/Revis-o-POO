import math

class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def radiciacao(self, a):
        return math.sqrt(a)

    def fatorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.fatorial(n - 1)

# Exemplo de uso
calc = Calculadora()

# Operações básicas
print(f"Soma: {calc.soma(5, 3)}")
print(f"Subtração: {calc.subtracao(10, 4)}")
print(f"Multiplicação: {calc.multiplicacao(6, 7)}")

# Radiciação
print(f"Raiz quadrada de 25: {calc.radiciacao(25)}")

# Fatorial
numero = int(input("Digite um número para calcular o fatorial: "))
print(f"Fatorial de {numero}: {calc.fatorial(numero)}")
