import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Aluno:
    nome: str
    idade:int
    email: str
    telefone: float

QUANTIDADE_ALUNOS = 2
lista_alunos = []

print("Solicitando dados dos alunos.")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite sua idade: ")),
        email= input("Digite seu endereço de e-mail: "),
        telefone= float(input("Digite seu número de telefone: "))
    )
    lista_alunos.append(aluno)

print()
print("Salvando dados.")
arquivo = "dados_alunos.txt"

with open(arquivo, "a") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}, {aluno.email}, {aluno.telefone} \n")
    print("Salvo com sucesso!")
