import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class usuario:
    nome: str
    email: str
    telefone: float
    endereco: str

usuario1 = usuario(nome = input("Digite seu  nome: "),
                   email = input("Digite seu e-mail: "),
                   telefone = float(input("Digite seu número de telefone: ")),
                   endereco = input("Digite seu Endereço: "))
import os
os.system("cls")
print(f"\nNome: {usuario1.nome} \nE-mail: {usuario1.email} \nTelefone: {usuario1.telefone} \nEndereço: {usuario1.endereco}")