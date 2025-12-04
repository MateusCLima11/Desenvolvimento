import os
from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str

@dataclass
class Cliente:
    nome: str
    email: str

cliente1 = Cliente(nome= input("Digite seu nome: "),
                 email= input("Digite seu e-mail: "))

endereco1 = Endereco(logradouro= input("Digite "),
                    numero= int(input("Digite o número da sua residência: ")),
                    cidade= input("Digite sua cidade: "))


