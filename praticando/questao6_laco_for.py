import os
os.system ("cls")

#Escreva um algoritmo que solicite ao usuário 5 valoresinteiros e ao final mostre:
#quantos números são pares e quantos números são ímpares;

pares = 0
impares = 0

for i in range(5):
    numero = int(input(f"Digite seu {i+1}º numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n Resultado")
print(f"\n Quantidade de numeros pares: {pares}")
print(f"\n Quantidade de numeros impares: {impares}")