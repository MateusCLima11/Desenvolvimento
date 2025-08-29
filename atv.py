import os
os.system ("cls")

login_slv = "Vasco"
senha_slv = "Rebaixamento"

login = input("Insira seu login: ")
senha = input("Insira sua senha: ")

if login_slv == login and senha_slv == senha:
    print("Bem-Vindo a segunda divisão!")
else:
    print("Acesso Negado")