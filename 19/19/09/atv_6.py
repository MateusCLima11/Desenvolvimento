import os 
os.system

soma = 0
qnt_num = 0

while True:
    numero = int(input("Digite o numero desejado: "))

    if numero < 0:
        break

    soma += numero
    qnt_num += 1

media = soma / qnt_num

print(f"A Média dos números informados é: {media:.2}")