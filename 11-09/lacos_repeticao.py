import streamlit as st
st.title("Verificando média")
media = st.number_input("Digite a média: ")
if st.button("Verificar"):


    if media >= 7:
        st.write("Aprovado!")
    else:
        st.write("Reprovado!")
else:
        st.warning("Informe a média.")

        #sucess - verde
        #warning - amarelo
        #info - azul
        #error - vermelho