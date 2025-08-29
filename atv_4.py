import os
os.system ("cls")

n1 = ("Digite o primeiro numero: ")
n2 = ("Digite o awgundo numero: ")

operacao = ("Digite a operação desejada: ")

match operacao:
    case "+":
        soma = n1 + n2
        print(f"Soma é igual a:{soma}")
    case "-":
        subtracao = n1 - n2
        print(f"Subtração é igual a:{subtracao}")