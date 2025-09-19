import os 
os.system

soma = 0
quantidade_notas = 0

while True:
    nota = float(input("Digite uma nota: "))
    quantidade_notas += 1
    soma += nota

    reposta = input("Deseja inserir mais umanota ? \n S ou N: ").upper()
    
    if reposta == "N":
        break

media = soma / quantidade_notas

print(f"\nMédia: {media:.2}")