import os
os.system ("cls")

#Escrever um programa de computador que solicite do
#usuário 5 números inteiros e, ao final, apresente a
#soma de todos os números lidos.

soma = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1} desejado: "))
    soma += numero

print(f"A soma dos numeros informados é: {soma}")