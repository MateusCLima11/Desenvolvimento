
from dataclasses import dataclass

#Estrutura de dados: classe.
@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str
@dataclass
class Pet:
    nome: str
    idade: int   
    peso: float
#Exemplo de uso da classe
pessoa1 = Pessoa(nome="Alice",idade=30, cpf="123.456.789-10")
pet1 = Pet(nome="Bob",idade=4,peso=2.100 )

print("Exibindo dados da pessoa.")
print(f"Nome:{pessoa1.nome}, Idade {pessoa1.idade}, CPF: {pessoa1.cpf}")
print("Exibindo dados do pet. ")
print(f"Nome: {pet1.nome}, Idade {pet1.idade} Peso: {pet1.peso}")