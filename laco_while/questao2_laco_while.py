import os
os.system ("cls")

#Escreva um algoritmo que solicite ao usuário a nota de um aluno. 
#Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
#Mostre a nota informada pelo usuário.

# Solicita a primeira nota com validação
nota1 = float(input("Digite a primeira nota (0 a 10): "))
while nota1 < 0 or nota1 > 10:
    print("Nota inválida. Tente novamente.")
    nota1 = float(input("Digite a primeira nota (0 a 10): "))

# Solicita a segunda nota com validação
nota2 = float(input("Digite a segunda nota (0 a 10): "))
while nota2 < 0 or nota2 > 10:
    print("Nota inválida. Tente novamente.")
    nota2 = float(input("Digite a segunda nota (0 a 10): "))

# Calcula e exibe a média
media = (nota1 + nota2) / 2
print(f"A média do aluno é: {media:.2f}")
