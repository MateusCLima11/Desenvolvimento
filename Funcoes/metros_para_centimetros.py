import os
os.system
def converter_metros_centimetros(n1):
    return n1 * 100

metros = float(input("Digite o valor em metros: "))

valor_centimetros = converter_metros_centimetros(metros)

def mostrar_conversao(valor_centimetros):
    print(f"O resultado da conversão é: {valor_centimetros:.0f} cm")

mostrar_conversao(valor_centimetros)