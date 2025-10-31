import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Autor:
    nome: str
    autor: str
    preco: float
    categoria: str

QUANTIDADE_DADOS = 3
lista_alunos = []

print("Solicitando dados dos alunos.")
for i in range(QUANTIDADE_DADOS):
    autor1 = Autor(
        nome= input("Digite nome do livro: "),
        autor= input("Digite o nome do autor: "),
        preco= float(input("Digite o preço do livro: ")),
        categoria= input("Digite a categoria do livro: ")
    )
    lista_alunos.append(autor1)

print()
print("Salvando dados.")
arquivo = "catalogo_livros.txt"

with open(arquivo, "a") as arquivo_alunos:
    for autor1 in lista_alunos:
        arquivo_alunos.write(f"{autor1.nome}, {autor1.autor}, {autor1.preco}, {autor1.categoria} \n")
    print("Salvo com sucesso!")
