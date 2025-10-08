import os
import time

os.system("cls")

#Criando uma função.

def saudacao():
    print("Boa tarde!")
    time.sleep(3) #espera 3 segundos.
    os.system("cls")

#Codigo principal>
saudacao() #Chamando a função.
print("Exemplo de uso de uma função sem parâmetros.")