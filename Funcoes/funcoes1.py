import os
os.system("cls")

#Funcao com passagem de parametros.
#Criando uma funcao.
def saudacao(nome, idade):
    print(f"Olá, {nome}! Bem-vindo(a)!")
    print(f"Sua iadade é {idade} anos.")
    
print("Solicitando dados.")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

#Chamando a funcao.
saudacao(nome, idade)
