import os
os.system ("cls")

#Escrever um programa de computador que solicite do usuário 3 notas e, ao final,
#apresente a média e mostre para o usuário se o aluno está aprovado, em recuperação ou reprovado.
#Considere que para aprovação, deve-se obter média maior ou igual a 7, para ser reprovado, a média deve ser menor que 4.

soma = 0

for i in range(3):
    nota = float(input(f"Digite sua {i+1}ª nota: "))
    soma += nota

media = soma / 3

if media >= 7:
    print("APROVADO!")
elif media >= 4:
    print("RECUPERAÇÃO.")
else:
    print("REPROVADO.")