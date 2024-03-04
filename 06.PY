import re

class CPFValidator:
    def __init__(self, cpf):
        self.cpf = cpf

    def validar_cpf(self):
        cpf = self.cpf.replace(".", "").replace("-", "")

        if len(cpf) != 11 or not cpf.isdigit():
            return False

        cpf_numeros = [int(digito) for digito in cpf]

        # Calculando o primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += cpf_numeros[i] * (10 - i)
        resto = soma % 11
        if resto < 2:
            digito_verificador_1 = 0
        else:
            digito_verificador_1 = 11 - resto

        if digito_verificador_1 != cpf_numeros[9]:
            return False

        # Calculando o segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += cpf_numeros[i] * (11 - i)
        resto = soma % 11
        if resto < 2:
            digito_verificador_2 = 0
        else:
            digito_verificador_2 = 11 - resto

        if digito_verificador_2 != cpf_numeros[10]:
            return False

        return True

    def validar_cpf_regex(self):
        cpf_regex = re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$")
        if not cpf_regex.match(self.cpf):
            return False

        cpf = self.cpf.replace(".", "").replace("-", "")

        cpf_numeros = [int(digito) for digito in cpf]

        # Verificando se todos os dígitos são iguais
        if len(set(cpf_numeros)) == 1:
            return False

        # Calculando o primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += cpf_numeros[i] * (10 - i)
        resto = soma % 11
        if resto < 2:
            digito_verificador_1 = 0
        else:
            digito_verificador_1 = 11 - resto

        if digito_verificador_1 != cpf_numeros[9]:
            return False

        # Calculando o segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += cpf_numeros[i] * (11 - i)
        resto = soma % 11
        if resto < 2:
            digito_verificador_2 = 0
        else:
            digito_verificador_2 = 11 - resto

        if digito_verificador_2 != cpf_numeros[10]:
            return False

        return True

def main():
    cpf = input("Digite o CPF (formato xxx.xxx.xxx-xx): ")
    cpf_validator = CPFValidator(cpf)
    if cpf_validator.validar_cpf():
        print("CPF válido!")
    else:
        print("CPF inválido!")

    if cpf_validator.validar_cpf_regex():
        print("CPF válido (usando RegEx)!")
    else:
        print("CPF inválido (usando RegEx)!")


if __name__ == "__main__":
    main()