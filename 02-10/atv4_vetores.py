import os
os.system("cls")

v_notas = []

quant = int(input("Digite a quantidade de notas:\n"))

for i in range (quant):
    nota=float(input(f"Digite a {i+1}° nota:\n"))
    print("")
    v_notas.append(nota)
    os.system("cls")
    
for i in range(quant):
    print(f"{i+1}° nota: {v_notas[i]:.2f}\n ")
soma=sum(v_notas)
media=soma/quant
menor=min(v_notas)
maior=max(v_notas)

print(f"Média: {media:.2f}\n ")
print(f"A menor nota: {menor:.2f}\n ")
print(f"A maior nota: {maior:.2f}\n ")

if media >= 7.00:
    print("Aluno Aprovado!!!")
elif media >= 5.00:
    print("Aluno em Recuperação!!!")
else:
    print("Aluno Reprovado!!!")