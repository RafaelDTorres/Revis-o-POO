import datetime

class CalculadoraDatas:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def calcular_diferenca(self):
        diferenca = self.data2 - self.data1
        return abs(diferenca.days)  # Valor absoluto para garantir que seja positivo

# Solicita as datas de entrada ao usuário
try:
    data1_str = input("Digite a primeira data (formato: dd/mm/aaaa): ")
    data2_str = input("Digite a segunda data (formato: dd/mm/aaaa): ")

    data1 = datetime.datetime.strptime(data1_str, "%d/%m/%Y").date()
    data2 = datetime.datetime.strptime(data2_str, "%d/%m/%Y").date()

    calc = CalculadoraDatas(data1, data2)
    diferenca_dias = calc.calcular_diferenca()
    print(f"A diferença entre as datas é de {diferenca_dias} dias.")
except ValueError:
    print("Formato de data inválido. Use o formato dd/mm/aaaa.")
