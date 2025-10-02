import os
os.system ("cls")

#criando um vetor.
quantidade_numeros = 6
lista_numeros = []
pares = 0
impares = 0

print(f"Solicitando {quantidade_numeros} números.")
for i in range(quantidade_numeros):
    numero = float(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    lista_numeros.append(numero)

    print("\nMostrando todos os numeros: ")

    for numero in lista_numeros:
        print(f"Numero: {numero}")

    print(f"Quantidade pares: {pares}")
    print(f"Quantidade impares: {impares}")