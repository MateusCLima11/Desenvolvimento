import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    cpf: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefoone: {self.telefone}")

    def dados_sms_marketing(self):
        print(f"Telefone: {self.telefone}")

lista_pessoas = []

for i in range(3):
    dados_pessoas = Pessoa(nome= input("Digite seu nome: "),
                           cpf= input("Digite seu CPF: "),
                           telefone= input("Digite se telefone: "))
lista_pessoas.append(dados_pessoas)  

for Pessoa in lista_pessoas:
        dados_pessoas.mostrar_dados()