import os
import time

# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(3) # Espera 3 segundos.
    os.system("cls")

# Função com parâmetros e com retorno.
def calcular_media(n1, n2):
    media = (n1 + n2) / 2

# Função com parâmetros e sem retorno.
def mostrar_resultado(media):
    print(f"Resultado: {media}")
    if media >= 7:
        print(f"Aprovado!:{media}")
    else:
        print(f"Reprovado!: {media}")

# Código principal.
# Função sem parâmetros e sem retorno.
limpa_tela() # Chamando a função.

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

# Função com parâmetros e com retorno.
media = calcular_media(primeiro_numero, segundo_numero)

# Função com parâmetros e sem retorno.
mostrar_resultado(media) # Chamando a função.