import os
os.system("cls")

#Funcao com passagem de parametros.
#Criando uma funcao.
def saudacao(nome, idade, altura, peso):
    print(f"Olá, {nome}! Bem-vindo(a)!")
    print(f"Sua idade é {idade} anos.")
    print(f"Sua altura é {altura}cm")
    print(f"Seu peso é {peso}kg")
    
print("Solicitando dados.")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = int(input("Digite sua altura em cm: "))
peso = float(input("Digite seu peso em KG:"))
#Chamando a funcao.
saudacao(nome, idade, altura, peso)
