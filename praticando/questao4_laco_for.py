import time

#Escrever um algoritmo que solicite ao usuário um
#número e faça a contagem regressiva a partir do
#número informado até o número 1, aguardando um
#segundo para exibir cada número.

numero = int(input("Digite o numero desejado para inicio da contagem regressiva: "))

for i in range (numero, 0, -1):
    print(i)
    time.sleep(1)