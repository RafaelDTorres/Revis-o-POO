import math

class CalculadoraGeometrica:
    def calcular(self, *args):
        num_args = len(args)

        if num_args == 1 and isinstance(args[0], float):
            # Área do círculo: A = π * r^2
            raio = args[0]
            return math.pi * raio**2

        elif num_args == 2 and all(isinstance(arg, float) for arg in args):
            # Área do quadrado: A = lado^2
            lado1, lado2 = args
            return lado1 * lado2

        elif num_args == 3 and all(isinstance(arg, int) for arg in args):
            # Perímetro do triângulo: P = a + b + c
            a, b, c = args
            return a + b + c

        elif num_args == 2 and isinstance(args[0], int) and isinstance(args[1], float):
            # Área do triângulo: A = (base * altura) / 2
            base, altura = args
            return (base * altura) / 2

        elif num_args == 3 and all(isinstance(arg, list) and len(arg) == 2 for arg in args):
            # Área do triângulo com coordenadas cartesianas
            x1, y1 = args[0]
            x2, y2 = args[1]
            x3, y3 = args[2]
            return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

        else:
            return "Uso incorreto. Forneça os argumentos corretos."

# Solicita os números de entrada ao usuário
try:
    raio = float(input("Digite o raio do círculo: "))
    lado1 = float(input("Digite o primeiro lado do quadrado: "))
    lado2 = float(input("Digite o segundo lado do quadrado: "))
    a = int(input("Digite o primeiro lado do triângulo: "))
    b = int(input("Digite o segundo lado do triângulo: "))
    c = int(input("Digite o terceiro lado do triângulo: "))
    base = int(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    vertices = []
    for i in range(3):
        x = float(input(f"Digite a coordenada x do vértice {i+1}: "))
        y = float(input(f"Digite a coordenada y do vértice {i+1}: "))
        vertices.append([x, y])

    calc = CalculadoraGeometrica()
    print(f"Área do círculo: {calc.calcular(raio)}")
    print(f"Área do quadrado: {calc.calcular(lado1, lado2)}")
    print(f"Perímetro do triângulo: {calc.calcular(a, b, c)}")
    print(f"Área do triângulo: {calc.calcular(base, altura)}")
    print(f"Área do triângulo com coordenadas cartesianas: {calc.calcular(*vertices)}")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números corretos.")
