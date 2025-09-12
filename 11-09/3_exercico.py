import streamlit as st

st.title("Verificação de números pares e impares")

paress = 0
impares = 0

for i in range(1,6):
    numero = st.number_input("Digite o {i}º Número: ", step=1)
    if numero % 2 == 0:
        pares = pares + 1
    else:
        imapares = impares = 1
        
if st.button("Verificar"):
    st.info(f"Quantidade de pares: {pares}")
    st.info(f"Quantidade de números impares: {impares}")
    
    