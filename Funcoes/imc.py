import os
os.system ("cls")

# Solicita os dados do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o IMC
print(f"Seu IMC é: {imc:.2f}")

# Classifica o IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
    recomendacao = "Consulte um nutricionista para orientação"
elif 18.5 <= imc <= 24.9:
    classificacao = "Peso normal"
    recomendacao = "Mantenha hábitos saudáveis"
elif 25.0 <= imc <= 29.9:
    classificacao = "Sobrepeso"
    recomendacao = "Cuide da alimentação e pratique atividade física"
elif 30.0 <= imc <= 34.9:
    classificacao = "Obesidade grau 1"
    recomendacao = "Consulte um nutricionista"
elif 35.0 <= imc <= 39.9:
    classificacao = "Obesidade grau 2"
    recomendacao = "Consulte um nutricionista"
else:
    classificacao = "Obesidade grau 3"
    recomendacao = "Consulte um nutricionista"

# Exibe os resultados
print("Exibindo dados")
print(f"IMC {imc}")
print(f"Classificação: {classificacao}")
print(f"Recomendação: {recomendacao}")