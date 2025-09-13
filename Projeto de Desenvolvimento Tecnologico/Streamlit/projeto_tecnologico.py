import streamlit as st
from analisesFinanceiras.analise1 import run as analise1_run
from analisesFinanceiras.analise2 import run as analise2_run
from analisesFinanceiras.analise3 import run as analise3_run
from analisesFinanceiras.analise4 import run as analise4_run        

JSON_PATH = "../input/Projetos de Desenvolvimento Tecnologico.json"

st.set_page_config(page_title="Projeto de Desenvolvimento Tecnológico", page_icon="../../images/upeLogo.png" ,layout="wide")
st.title("Projeto de Desenvolvimento Tecnológico: Data Analysis Dashboard")

st.sidebar.image("../../images/upeLogo.png", width=200)
st.sidebar.title("Navegação entre Dashboards")
pagina = st.sidebar.radio(
    "Selecione uma análise",
    ["Análise 1: Comparativo mensal de valores ao longo de 1 ano", 
     "Análise 2: Somatório anual por projeto", 
     "Análise 3: Total Mensal de Todos os Projetos", 
     "Análise 4:    Recebimentos anuais por órgão (Agência, Unidade, IA-UPE)"],
    index=0,
)

if pagina.startswith("Análise 1"):
    analise1_run(JSON_PATH)
elif pagina.startswith("Análise 2"):
    analise2_run(JSON_PATH)
elif pagina.startswith("Análise 3"):
    analise3_run(JSON_PATH)
elif pagina.startswith("Análise 4"):
    analise4_run(JSON_PATH)
else:
    st.error("⚠️Página não encontrada.")