import os
os.system("cls") 

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Usuario:
    nome: str
    data_nascimento: str
    rg: float
    cpf: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nData de nascimento: {self.data_nascimento} \nRG: {self.rg} \nCPF: {self.cpf}\n")

lista_dados = []
QUANTIDADE_USUARIOS = 3

for i in range(QUANTIDADE_USUARIOS):
    usuario = Usuario(
        nome= input("Digite seu nome: "),
        data_nascimento= input
    )