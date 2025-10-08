import os
os.system("cls")

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
  return n1 - n2

def dividir(n1, n2):
  return n1 / n2

def multiplicar(n1, n2):
  return n1 * n2

def mostrar_resultado(soma, subtracao, divisao, multiplicacao):
   print(f"O resultado da soma é:{soma}")
   print(f"O resultado da subtração é:{subtracao}")
   print(f"O resultado da divisão é: {divisao}")
   print(f"O resultado da multiplicação é: {multiplicacao}")

primeiro_numero = int(input("Digite seu primero número: "))
segundo_número = int(input("Digite seu primeiro número: "))

soma = somar(primeiro_numero, segundo_número)
subtracao = subtrair(primeiro_numero, segundo_número)
divisao = dividir(primeiro_numero, segundo_número)
multiplicacao = multiplicar(primeiro_numero, segundo_número)

mostrar_resultado(soma, subtracao, divisao, multiplicacao)