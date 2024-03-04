class NumerosPrimos:
    def __init__(self):
        pass

    def eh_primo(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def contaPrimos(self, inicio, fim):
        count = 0
        for num in range(inicio, fim + 1):
            if self.eh_primo(num):
                count += 1
        return count

# Solicita os números de entrada ao usuário
try:
    inicio = int(input("Digite o primeiro número inteiro positivo: "))
    fim = int(input("Digite o segundo número inteiro positivo (maior que o primeiro): "))
    if inicio >= fim:
        print("O segundo número deve ser maior que o primeiro.")
    else:
        obj = NumerosPrimos()
        quantidade_primos = obj.contaPrimos(inicio, fim)
        print(f"Quantidade de números primos entre {inicio} e {fim}: {quantidade_primos}")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números inteiros positivos.")
