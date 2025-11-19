import os
os.system("cls") 

from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} /nIdade: {self.idade}\n")

lista_de_pacientes = []
QUANTIDADE_DE_PACIENTES = 2

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite sua idade: "))
    )
    lista_de_pacientes.append(paciente)
    print() #pula uma linha.

    nome_do_arquivo = "dados_pacientes.csv"
    with open(nome_do_arquivo, "a") as arquivo_pacientes:
        for paciente in lista_de_pacientes:
            arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}")
            print("Dados salvos com sucesso.")

print("\nExibindo lista de pacientes: ")
lista = []
try:
    #"r" - read - leitura
    with open(nome_do_arquivo, "r") as arquivo:
        #Recebe todos os dados do arquivo de uma só vez.
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes:
            nome, idade = paciente.strip().split(",")
            dados_paciente = Paciente(nome=nome, idade=int(idade))
            lista.append(dados_paciente)
    for paciente in lista:
        paciente.exibir_dados()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")