import os
os.system ("cls")

somatotal = 0

paresmedia = 0

mediatotal = 0

while True:
    numero = int(input("Digite o numero desejado: "))
    if numero < 0:
        break

    if numero % 2 ==0:
        paresmedia