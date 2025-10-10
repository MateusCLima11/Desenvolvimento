import os
os.system

print("""     Laço de repetição     """)

#("Crie um programa que solicite ao usuário seu login e uma senha." \
#"O programa deve continuar pedindo o login e a senha até que ambos estejam corretos.")

slv_login = input("Crie nome para login: ")
slv_senha = int(input("Crie senha para login: "))

while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha :")
    if slv_login == login and slv_senha == senha:
        print("Login Realizado Com Sucesso!")
        break
    else:
        print("Login ou Senha Incorreto.")