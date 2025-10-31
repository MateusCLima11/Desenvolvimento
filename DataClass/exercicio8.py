import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int

    def mostrar_endereco(self):
        print("Exibindo Endereço:")
        print(f"Logradouro: {self.logradouro}")
        print(f"Número: {self.numero}")


@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco

    def mostrar_dados(self):
        print("Exibindo Endereço:")
        print(f"Logradouro: {self.nome}")
        print(f"Idade: {self.idade}")



endereco1 = Endereco(logradouro= input("Digite seu logradouro: "),
                     numero= int(input("Digite o número de seu endereço: ")))

pessoa1 = Pessoa(nome= input("Digite seu nome:"),
                 idade= int(input("Digite sua idade: ")))

import os
os.system ("cls")

pessoa1.mostrar_dados()
endereco1.mostrar_endereco()