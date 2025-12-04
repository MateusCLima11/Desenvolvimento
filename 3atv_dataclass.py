import os
import time
from dataclasses import dataclass
os.system("cls || clear") # Limpa o terminal em Windows Linux.

ista_clientes = []

@dataclass
class Cliente:
    # Atributos da classe.
    # Atributos são variavéis que pertecem à classe.
    nome: str
    email: str
    telefone: str

    # Método para mostrar as informações dos clientes.
    # Método é o nome dado a uma função que pertence à classe.
    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nE-mail: {self.email} \nTelefone: {self.telefone}")


# Função para verificar se a lista está vazia.
def lista_esta_vazia(lista_clientes):
    if not lista_clientes:
        print("\nNão há clientes cadastrados.")
        return True
    return False

# Função para adicionar novos clientes na lista.
def adicionar_cliente(lista_clientes):
    print("\n--- Adicionar novo cliente ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f"\nCliente {nome} adicionado com sucesso!")

# Função para encontrar um cliente na lista.
def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for cliente in lista_clientes:
        if cliente.nome.lower.lower() == nome_buscar_lower:
            return cliente
    return None # None significa retornar vazio, sem conteúdo.

# Função para mostrar todos os clientes.
def mostrar_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    print("\n--- Lista de Clientes ---")
    for cliente in lista_clientes:
        print(f"{cliente.mostrar_dados()}")

# Função para atualizar clientes.
def atualizar_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    # Mostrar a lista para ajudar o usuário.
    mostrar_todos_clientes(lista_clientes)
    print("--- Atualizar dados do cliente ---")
    nome_buscar = input("\n Digite o nome do cliente: ")
    cliente_para_atualizar = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_atualizar:
        print("\nPessoa encontrada.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nE-mail atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo e-mail: ")

        print(f"Telefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone = input("Novo telefone: ")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_telefone:
            cliente_para_atualizar = novo_telefone

        print(f"\nDadps do cliente: {nome_buscar} atualizados com sucesso!")
    else:
        print(f"\nClienre com nome: {nome_buscar} não encontrado")