import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome = str
    email = str
    endereco = str

    def mostrar_dados(self):
        print("Exibindo dados do usuário")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco}")

    def mostrar_nome(self):
        print("Exibindo apenas nome do usuário")
        print(f"Nome: {self.nome}")

pessoa1 = Pessoa(nome= input("Digite seu nome"),
                 email= input("Digite seu e-mail: "),
                 endereco= input("Digite seu endereço: "))

pessoa2 = Pessoa(nome= input("Digite seu nome"),
                 email= input("Digite seu e-mail: "),
                 endereco= input("Digite seu endereço: "))

pessoa1.mostrar_dados
pessoa1.mostrar_nome

pessoa2.mostrar_dados
pessoa2.mostrar_nome
