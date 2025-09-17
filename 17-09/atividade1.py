import os
os.system ("cls")

slv_login = input("Crie seu login: ")
slv_senha = input("Crie sua senha: ")



while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    if slv_login == login and slv_senha == senha:
        break
    else:
        print("Login e/ou senha incorretos.")
