import os
os.system("cls || clear")
from dataclasses import dataclass

lista_fun = []
lista_cli = []

@dataclass
class Funcionarios:
    nome_: str
    data_de_admissao: str
    matricula_: str
    endereco_: str
    def dados_dos_funcionarios(self):
        print("\n\n======================")
        print("\nDados dos funcionários\n")
        print("======================")
        print(f"Nome: {self.nome_}\nData de admissão: {self.data_de_admissao}\nMatrícula: {self.matricula_}\nEndereço: {self.endereco_}")
        print("======================\n\n")

@dataclass
class Clientes:
    _nome: str
    data_de_nascimento: str
    _endereco: str
    def dados_dos_clientes(self):
            print("\n\n======================")
            print("\n= Dados dos Clientes =\n")
            print("======================")
            print(f"Nome: {self._nome}\nData de admissão: {self.data_de_nascimento}\nEndereço: {self._endereco}")
            print("======================\n\n")

quant = 3

for i in range (quant):
    print("=============")
    print("===Sistema===")
    print("=============")
    nome1=input("Digite o nome do funcionário:\n")
    print("=============")
    data_de_admissao1=input("Digite a data de admissão(dd/mm/aa):\n")
    print("=============")
    matricula1=input("Digite a matrícula do funcionario:\n")
    print("=============")
    endereco1=input("Digite o endereço do funcionário:\n")
    print("=============")
    funcionario1=Funcionarios(nome_=nome1,data_de_admissao=data_de_admissao1,matricula_=matricula1,endereco_=endereco1)
    lista_fun.append(funcionario1)
    os.system("cls || clear")


for i in range (quant):
    print("=============")
    print("===Sistema===")
    print("=============")
    nome2=input("Digite o nome do cliente:\n")
    print("=============")
    data_de_nascimento1=input("Digite a data de nascimento(dd/mm/aa):\n")
    print("=============")
    endereco2=input("Digite o endereço do cliente:\n")
    print("=============")
    cliente1=Clientes(_nome=nome2,data_de_nascimento=data_de_nascimento1,_endereco=endereco2)
    lista_cli.append(cliente1)
    os.system("cls || clear")


for Funcionarios in lista_fun:
    Funcionarios.dados_dos_funcionarios()

for Clientes in lista_cli:
    Clientes.dados_dos_clientes()

nome_arq_fun="tabela_de_dados_funcionários.csv"
with open(nome_arq_fun, "a", encoding="utf-8") as arquivo_tabfun:
     for Funcionarios in lista_fun:
        arquivo_tabfun.write(f"{Funcionarios.nome_}\n{Funcionarios.data_de_admissao}\n{Funcionarios.matricula_}\n{Funcionarios.endereco_}\n\n")
        print("============")
        print("Dados salvos")
        print("============")

nome_arq_cli="tabela_de_dados_clientes.csv"
with open(nome_arq_cli, "a", encoding="utf-8") as arquivo_tabcli:
     for Clientes in lista_cli:
        arquivo_tabcli.write(f"{Clientes._nome}\n{Clientes.data_de_nascimento}\n{Clientes._endereco}\n\n")
        print("============")
        print("Dados salvos")
        print("============")
        