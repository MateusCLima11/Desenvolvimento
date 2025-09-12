import streamlit as st 

st.title("Escreva um programa de computador que solicite do usuário 4 notas e ao final apresente a média.")

for i in range(1,5):
    nota = st.number_input("Digite a {i}ª nota")
    media = nota/4
if st.button("Calcular"):
    st.info(f"A média igual a:{media}")