import os
os.system ("cls")

#Escrever um programa de computador que solicite do usuário 4 notas e
#ao final, apresente a média.

soma = 0

for i in range(4):
    nota = float(input(f"Digite sua {i+1}ª nota: "))
    soma += nota
    
media = soma / 4

print(f"A media das notas digitadas é: {media:.2f}")