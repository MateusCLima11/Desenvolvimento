import os
os.system ("cls")
from dataclasses import dataclass

@dataclass
class dados:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostrando_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")

lista_de_pessoas = []

for i in range (3):
    dados_cliente= dados(nome=input("Digite seu nome"),
                         idade=int(input("Digite sua idade: ")),
                         peso=float(input("Digite seu Peso: ")),
                         altura=float(input("Digite sua Altura: ")))
    lista_de_pessoas.append(dados_cliente)
    os.system("cls")

for dados in lista_de_pessoas:
    dados_cliente.mostrando_dados()