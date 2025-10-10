import os
os.system("cls")

#Escreva um algoritmo que solicite do usuário um número e mostre 
# a tabuada de multiplicação do número informado.

numero = int(input("Digite um número para que seja realizada a tabuada de 1 a 10: "))

print(f"Tabuada do {numero}:")

for i in range(1,11):
    tabuada = numero * i
    print(f"{numero} x {i} = {tabuada}")