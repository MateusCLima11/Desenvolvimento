import streamlit as st 

st.title("Escreva um programa de computador que solicite do usuario 3 notas e ao final apresente a média e mostre para o usuario se o launo esta aprovado, em recuperação ou reprovado.")

st.header("Contador de Média.")

QUANTIDADE_NOTAS = 3
soma = 0 

for i in range(QUANTIDADE_NOTAS)
    nota = st.number_input(f"Digite {i+1}ª nota: ")
    soma = soma + nota
    
media = soma / QUANTIDADE_NOTAS

if st.button("Mostrar resultado"):
    st.info(f"Média: {media:.2}")
    if media >= 7:
        st.success(f"Aprovado")
    elif media >= 4:
        st.warning(f"Recuperação")
    else:
        st.error(f"Reprovado")