import streamlit as st
import time

st.title("Laço de Repetição: FOR")

st.write("Escreva um algoritimo que mostra os números ímpares entre 1 e 20")
st.write("Prima o botão para iniciar")

if st.button("Iniciar"):
    for i in range (1,21, 2):
        st.info(i)
        time.sleep(1)
    st.header("FIM")