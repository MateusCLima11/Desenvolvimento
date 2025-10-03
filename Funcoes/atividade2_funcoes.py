import os
os.system

def positivo_ou_negativo(numero):
    if numero < 0:
        print("Negativo")
    else:
        print("Positivo")
        
print("Solicitando dados")
numero = int(input("Digite o numero desejado: "))

positivo_ou_negativo(numero)