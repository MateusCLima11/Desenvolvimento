import os
os.system("cls") 
from dataclasses import dataclass

lista_dados_funcionario = []

@dataclass
class Funcionario:
    nome: str
    data_admissao: str
    matricula: float
    endereco: str

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nData de Admissão: {self.data_admissao} \nMatrícula: {self.matricula} \nEndereço: {self.endereco}\n")

@dataclass
class Clientes:
    nome = str
    data_nascimento = str
    endereco = str

    def mostrar_dados_clientes(self):
        print(f"Nome: {self.nome} \nData de Nascimento: {self.data_nascimento} \nEndereço: {self.endereco}")

QUANTIDADE_FUNCIONARIOS = 3
QUANTIDADE_CLIENTES = 3

for i in range(QUANTIDADE_FUNCIONARIOS):
    funcionario = Funcionario(
        nome= input("Digite seu nome: "),
        data_admissao= input("Digite sua data de admissão: "),
        matricula= float(input("Digite seu número de matrícula: ")),
        endereco= input("Digite seu endereço: ")
    )
    
for i in range(QUANTIDADE_CLIENTES):
    cliente = Clientes(
        nome= input("Digite seu nome: "),
        data_nascimento= input("Digite sua data de nascimento: "),
        endereco= input("Digite seu endereço: ")
    )

