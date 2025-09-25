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
     "Análise 4: Recebimentos anuais por órgão (Agência, Unidade, IA-UPE)"],
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




''''
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Projeto de Desenvolvimento Tecnológico",
    page_icon="images/upeLogo.png",
    layout="wide",
)

st.image("images/upeLogo.png", width=160)
st.title("Projeto de Desenvolvimento Tecnológico: Data Analysis Dashboard")

st.markdown(
    """
    Bem-vindo ao painel de análises.  
    Use o menu de **Páginas** (barra lateral) para escolher a análise desejada.
    """
)

st.divider()
st.subheader("Atalhos rápidos")

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/01_Analise_1.py", label="Análise 1 — Comparativo mensal de valores ao longo de 1 ano")
    st.page_link("pages/02_Analise_2.py", label="Análise 2 — Projetos por segmento/ano")
with col2:
    st.page_link("pages/03_Analise_3.py", label="Análise 3 — Total mensal de todos os projetos")
    st.page_link("pages/04_Analise_4.py", label="Análise 4 — Recebimentos anuais por órgão")
'''''''''