import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoas:
    nome: str
    cpf: str
    telefone: str

    def mostrar_dados(self):
        print("MOSTRANDO DADOS")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")

    def dados_sms_marketing(self):
        print("MOSTRAANDO TELEFONE")
        print(f"Telefone: {self.telefone}")


lista_pessoas = []

for i in range(3):
    dados_pessoas = Pessoas(nome= input("Digite seu nome: "),
                           cpf= input("Digite seu CPF: "),
                           telefone= input("Digite se telefone: "))
    lista_pessoas.append(dados_pessoas)  

import os
os.system("cls")

for dados_pessoas in lista_pessoas:
    dados_pessoas.mostrar_dados()