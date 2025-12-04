import os
from dataclasses import dataclass
os.system("cls")

QUANTIDADE_FUNCIONARIOS = 3
lista_funcionario = []

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    cpf: str
    funcao: str


    def mostrar_dados(self):
        print(f"Nome do Funcionário: {self.nome}")
        print(f"Data de nascimento do Funcionário: {self.data_nascimento}")
        print(f"CPF do funcionário: {self.cpf}")
        print(f"Função do funcionário: {self.funcao}")


print("Solicitando dados")
print("Solicitando dados dos alunos.")
for i in range(QUANTIDADE_FUNCIONARIOS):
    funcionario = Funcionario(nome= input("Digite seu nome: "),
                              data_nascimento= input("Digite sua data de nascimento: "),
                              cpf= input("Digite seu CPF: "),
                              funcao= ("Digite sua função: ")
    )
    lista_funcionario.append(funcionario)

print("Salvando dados...")
arquivo = "dados_funcionarios.txt"

with open(arquivo, "a") as arquivo_funcionarios:
    for funcionario in lista_funcionario:
        arquivo_funcionarios.write(f"{funcionario.nome}, {funcionario.data_nascimento}, {funcionario.cpf}, {funcionario.funcao} \n")
    print("Salvo com sucesso!")