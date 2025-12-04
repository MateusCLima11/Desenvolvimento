import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = Pessoa(nome=input("Digite seu nome: "), 
                 idade=int(input("Digite sua idade: ")), 
                 peso=float(input("Digite seu peso: ")), 
                 altura=float(input("Digite sua altura: ")))

#Exibir
print("Exibindo dados:")
print(f"\nNome:{pessoa1.nome}\nIdade: {pessoa1.idade} \nPeso: {pessoa1.peso} \nAltura: {pessoa1.altura}")