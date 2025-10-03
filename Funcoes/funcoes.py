import os 
os.system("cls")

#criando um função
def logo_senai():
    os.system("cls")
    print("=========")
    print("==senai==")
    print("=========")
    
logo_senai()
nome =  input("Digite seu nome: ")
logo_senai()
idade = int(input("digite sua idade: "))
logo_senai()
peso = float(input("digite sua peso: "))

logo_senai()
print(f"Nome: {nome}")
print(f"idade: {idade}")
print(f"peso: {peso}")