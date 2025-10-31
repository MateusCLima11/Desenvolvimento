import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Autor:
    nome: str
    biografia: str




@dataclass
class Livro:
    titulo: str
    ano: int
    autor:Autor

    def exibir_detalhes(self):
        print(f"Titulo do livro: {self.titulo}")
        print(f"Ano de publicação da obra: {self.ano}")
        print(f"Autor da obra: {self.autor}")

nome1=input("Digite o nome do autor: ")
biografia1=input("Escreva a biografia do autor: ")
titulo1=input("Digite o Título da requerida obra: ")
ano1= input("Digite o ano da requerida obra: ")

autor1 = Autor(nome=nome1,biografia=biografia1)
livro1=Livro(titulo=titulo1,ano=ano1,autor=autor1)

os.system("cls")

livro1.exibir_detalhes()