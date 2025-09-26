import os
os.system ("cls")

total_familias = 0
salario = 0
maior_salario = 0
menor_salario = 0
filhos = 0
salario_populacao = 0

while True:
    print("""
          codigo | Descrição
             1   | Adicionar familía
             2   | Sair e exibir resultados""")
    
    opcao = int(input("Digite o codigo desejado: "))

    
    match opcao:
        case 1:
            salario = float(input("Digite seu salario: "))
            filhos = int(input("Digite quantidade de filhos: "))

            total_familias += 1
            salario_populacao += salario

    if salario < menor_salario: