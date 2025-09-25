import streamlit as st
from analisesFinanceiras.analise1_comparativa import run as analise1_run
from analisesFinanceiras.analise2_somatorio import run as analise2_run
from analisesFinanceiras.analise3_total_mensal import run as analise3_run

st.set_page_config(page_title="PROPEGI Financeiro", page_icon="../../images/upeLogo.png" ,layout="wide")
st.title("PROPEGI Financeiro: Data Analysis Dashboard")

with st.sidebar: 
    st.image("../../images/upeLogo.png", width=200)  #Diminuir o Tamnanho da Logo
    st.header("Navegação entre Dashboards")
    escolha = st.radio(
        "Escolha a Análise:",
        options=[
            "Análise 1 - Comparativo de Valores das Folhas por Projeto (Mês/Ano)",
            "Análise 2 - Somatório de Valores das Folhas por Projeto",
            "Análise 3 — Total Mensal de Todos os Projetos",
        ],
        index=0  # Isso aqui vai me fazer abrir o streamlit direto na Análise 1
    )

if escolha.startswith("Análise 1"):
    analise1_run()
elif escolha.startswith("Análise 2"):
    analise2_run()
elif escolha.startswith("Análise 3"):
    analise3_run()
else:
    st.error("⚠️ Página não encontrada.")