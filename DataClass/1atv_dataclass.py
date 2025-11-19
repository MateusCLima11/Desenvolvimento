import os
from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: int
    cpf: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \nPeso:{self.peso} \nAltura: {self.altura} \nCPF: {self.cpf}")

lista_de_pacientes = []
QUANTIDADE_DE_PACIENTES = 2

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite sua idade: ")),
        peso= float(input("Digite seu peso: ")),
        altura= int(input("Digite sua altura em centímetros: ")),
        cpf= float("Digite seu CPF: "
        ))
    lista_de_pacientes.append(paciente)
    print() #pula uma linha.

    nome_do_arquivo = "dados_pacientes.csv"
    with open(nome_do_arquivo, "a") as arquivo_pacientes:
        for paciente in lista_de_pacientes:
            arquivo_pacientes.write(f"{paciente.nome}, \n{paciente.idade} \n{paciente.peso} \n{paciente.altura} \n {paciente.cpf}")
            print("Dados salvos com sucesso.")

print("\nExibindo lista de pacientes: ")
for paciente in lista_de_pacientes:
    paciente.exibir_dados()