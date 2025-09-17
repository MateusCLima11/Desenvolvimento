import streamlit as st

st.title("Laço de repetição")

st.write("Crie um programa que solicite ao usuário seu login e uma senha." \
"O programa deve continuar pedindo o login e a senha até que ambos estejam corretos.")

slv_login = st.text_input("Crie nome para login: ")
slv_senha = st.number_input("Crie senha para login: ")

while True:
    login = st.text_input("Digite seu login: ")
    senha = st.number_input("Digite sua senha :")
    if slv_login == login and slv_senha == senha:
        print("Login Realizado Com Sucesso!")
        break
    else:
        ("Login ou Senha Incorreto.")