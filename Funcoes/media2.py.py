import os
os.system("cls")
import time

lista_notas = []
def calcular_media(media):
    media = sum(lista_notas) / len(lista_notas)
    os.system("cls")
    time.sleep(3)
    return media
def aprovado_reprovado(media):
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    print(f"Sua media é {media:.2f} \nVocê está {resultado}")
    return resultado
media = 0
for i in range(1, 3):
    notas = float(input(f"Digite a {i}° nota: "))
    while notas < 0 or notas > 10:
        print("Digite um numero valido entre 0 e 10")
        notas = float(input(f"Digite a {i}° nota: "))
    lista_notas.append(notas)
media_final = calcular_media(lista_notas)
resultado_final = aprovado_reprovado(media_final)