import os
from dataclasses import dataclass
os.system("cls")

QUANTIDADE_CLIENTES = 3
lista_clientes = []

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: float
    endereço: str

QUANTIDADE_CLIENTES = 3
lista_clientes = []    

    def mostra_dados_clientes(self):
        print(===Exibindo dados dos clientes===)
        print(f"Nome do cliente: {self.nome} \nE-mail do cliente: {self.email} \nTelefone do cliente: {self.telefone} \nEndereço do cliente: {self.endereco}")

