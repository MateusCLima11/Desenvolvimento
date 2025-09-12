import streamlit as st 

st.title("Lógica de Programação")

while True:
    numero = st.number_input("Digite um número: ", step=1)
    if numero == 2:
        break
    
    st.header("Fim")