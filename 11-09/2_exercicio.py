#Escreva um algoritimo que solicite ao usuario um numero e mostre a tabuda de multiplicao do numero informado

import streamlit as st

num = st.number_input("Digite o numero desejado:\n",step=1)

if st.button("iniciar"):
    for i in range(1,11):
        s=num*i
        st.write(f"{num} x {i} = {s}")
    st.success("FIM")