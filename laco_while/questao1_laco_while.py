import os
os.system ("cls")

#Escreva um algoritmo que solicite ao usuário a nota de um aluno. 
#Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
#Mostre a nota informada pelo usuário.

nota = -1

while nota < 0 or nota > 10:
    nota = float(input("Digite a nota do aluno: "))
    print(f"Nota informada: {nota}")