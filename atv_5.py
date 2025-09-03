import os
os.system ("cls")

print(""""
      
codigo \t Prato \t \t Valor 
  1 \t Picanha \t 25,00 R$          
  2 \t Lasanha \t 20,00 R$
  3 \t Strogonoff \t 18,00 R$
  4 \t Bife Acebolado\t 15,00 R$
  5 \t Pão com Ovo \t 05,00 R$          
      """)

codigo = int(input("Digite o codigo do prato desejado: "))

match codigo:
    case 1:
        print("Prato selecionado: Picanha Valor: 25,00 R$")
    case 2:
        print("Prato selecionado: Lasanha Valor: 20,00 R$")
    case 3:
        print("Prato selecionado: Strogonoff Valor: 18,00 R$")
    case 4:
        print("Prato selecionado: Bife Acebolado Valor: 15,00 R$")
    case 5:
        print("Prato selecionado: Pão com Ovo Valor: 05,00 R$")