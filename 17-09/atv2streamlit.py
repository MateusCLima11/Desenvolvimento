import os
os.system ("cls")

tentativas = 0 
login_salvo = "marta"
senha_salva = "123"

while True:
    for i in range(3):
        print(f"Tentativa: {i+1}")
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == login_salvo and senha == senha_salva:
        print("Bem-vindo")
        break
    else:
        print("login ou senha ivalidos.\n")
    break