import  os
os.system("cls")

soma = 0
# inserindo notas:
for i in  range(3):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    soma += nota


#mostar notas>
print(f"Nota: {nota}")
print(f"soma: {soma}")


print("fim")
