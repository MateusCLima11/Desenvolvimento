import os

lista_notas = []

def media_nota(medias):
    medias = sum(lista_notas) / 3
    os.system("cls")
    print(f"A media das notas {lista_notas} = {medias:.2f}")
    return medias


for i in range(1, 4):
    nota = float(input(f"Digite a {i}° nota: "))
    lista_notas.append(nota)
resultado_media = media_nota(lista_notas)