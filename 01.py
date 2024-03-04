import re

class Cliente:
    def __init__(self, nome, endereco, cep, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__cep = cep
        self.__cpf = cpf

    # Métodos de acesso (getters)
    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_cep(self):
        return self.__cep

    def get_cpf(self):
        return self.__cpf

    # Métodos para alterar os atributos (setters)
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    def set_cep(self, novo_cep):
        # Validar o CEP usando RegEx (formato: XXXXX-XXX)
        if re.match(r"\d{5}-\d{3}", novo_cep):
            self.__cep = novo_cep
        else:
            print("CEP inválido. Formato esperado: XXXXX-XXX")

    def set_cpf(self, novo_cpf):
        # Validar o CPF usando RegEx (formato: XXX.XXX.XXX-XX)
        if re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", novo_cpf):
            self.__cpf = novo_cpf
        else:
            print("CPF inválido. Formato esperado: XXX.XXX.XXX-XX")

# Exemplo de uso
cliente1 = Cliente(nome="Maria Silva", endereco="Rua A, 123", cep="12345-678", cpf="123.456.789-01")
print(f"Nome: {cliente1.get_nome()}")
print(f"Endereço: {cliente1.get_endereco()}")
print(f"CEP: {cliente1.get_cep()}")
print(f"CPF: {cliente1.get_cpf()}")
