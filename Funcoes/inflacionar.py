import os
os.system('cls')

def inflacao(preco):
    if preco <= 100:
        print(f"P preço de {preco}R$ com inflação aplicada de 10% ficará: {preco + (10/100 * preco):.2f}R$")
    else:
        print(f"O preço de {preco}R% com inflacao aplicada de 20% ficará {preco + (20/100 * {preco}):.2f}R$")

preco = float(input("Digite o preço do produto em R$: "))

inflacao(preco)