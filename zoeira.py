import streamlit as st
import random

st.set_page_config(page_title="Portal da Diva", page_icon="💅")

st.title("💅 Questionário de Rotina da Diva")
st.subheader("Responda com sinceridade (se for capaz):")

# Pergunta de zoeira
st.write("### Você aceita lavar toda a louça do jantar hoje sem reclamar?")

# Criamos colunas para os botões
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("SIM, EU ACEITO"):
        st.balloons()
        st.success("Sábia decisão! Já deixei a esponja no jeito. ✨")

with col2:
    # A mágica acontece aqui: toda vez que a página recarrega, 
    # a posição do botão de "NÃO" pode mudar ou ele pode simplesmente não aparecer
    if "fugir" not in st.session_state:
        st.session_state.fugir = False

    # Se ela tentou clicar ou a página atualizou, o botão muda
    if st.button("NÃO"):
        st.session_state.fugir = True
        st.warning("ERRO 404: Opção inválida para divas. Tente novamente! 😂")
    
    if st.session_state.fugir:
        # Aqui a gente faz o botão "sumir" de um lugar e aparecer em outro aleatório
        st.write("Ops, o botão fugiu!")
        if st.button("NÃO (Tente aqui agora)"):
             st.error("Lenta demais! Tente o SIM.")