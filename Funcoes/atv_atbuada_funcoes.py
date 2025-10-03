import os
os.system

def mostrar_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range (1,11):
        tabuada = numero * i
        print(f"{i} x {numero} = {tabuada}")
        
print("Solicitando dados.")
numero = int(input("Digite o numero desejado para a tabuada: "))

mostrar_tabuada(numero)