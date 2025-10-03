import os
os.system

valores = []

print("Solicitando numeros")
for i in range (5):
    numero = int(input("Digite um numero: "))
    if numero > 0:
        numero = 0
    valores.append(numero)

for i, numero in enumerate(valores, start=1):
    print(f"{i}º Valor: {numero}")