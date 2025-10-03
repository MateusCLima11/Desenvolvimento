import os
os.system("cls")

#Funcao com passagem de parametros.
#criando funcao.
def par_ou_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")
        
print("Solicitando dados.")
numero = int(input("Digite um número"))

#chamando funcao.
par_ou_impar(numero)