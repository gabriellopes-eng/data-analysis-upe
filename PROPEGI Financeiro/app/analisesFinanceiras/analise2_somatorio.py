import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from .data_utils import carregar_financas_json, filtrar

# Caminho padrão: .../input/Financas.json (irmão da pasta Streamlit)
DEFAULT_JSON_PATH = Path(__file__).resolve().parents[2] / "input" / "Financas.json"

def run():
    st.header("◈ Análise 2: Somatório dos Valores das Folhas por projeto")

    # === Entrada do caminho do JSON (sem converter para CSV/Excel) ===
    caminho = st.text_input(
        "Caminho do Financas.json",
        value=str(DEFAULT_JSON_PATH),
        help="Se necessário, ajuste para o local onde o arquivo está."
    )

    # === Carregamento e tratamentos simples ===
    try:
        df = carregar_financas_json(caminho)
    except Exception as e:
        st.error(f"Erro ao carregar JSON: {e}")
        return

    # === Filtros simples: Ano e nome do projeto ===
    anos = sorted(df["Ano"].unique().tolist())
    col1, col2 = st.columns([2, 3])

    with col1:
        anos_sel = st.multiselect("Filtrar por Ano (opcional)", anos, default=anos)
    with col2:
        nome_filtro = st.text_input(
            "Filtrar por nome do projeto (contém, opcional)",
            value=""
        )

    df_filt = filtrar(df, anos_sel, None)
    if nome_filtro.strip():
        df_filt = df_filt[df_filt["Projetos"].str.contains(nome_filtro, case=False, na=False)]

    if df_filt.empty:
        st.warning("Sem dados para os filtros escolhidos.")
        return

    # === Agregação: soma do Valor da folha por Projeto ===
    soma_projeto = (
        df_filt.groupby("Projetos", as_index=False)["Valor da folha"]
        .sum()
        .rename(columns={"Valor da folha": "Total"})
        .sort_values("Total", ascending=True)   # para barras horizontais crescentes
    )

    # === Gráfico: Barras Horizontais (Plotly) ===
    fig = px.bar(
        soma_projeto,
        x="Total",
        y="Projetos",
        orientation="h",
        text="Total",
        labels={"Total": "Total (R$)", "Projetos": "Projetos"},
    )
    fig.update_traces(
        texttemplate="R$ %{x:,.2f}",
        hovertemplate="Projeto: %{y}<br>Total: R$ %{x:,.2f}<extra></extra>"
    )
    fig.update_layout(
        xaxis_tickformat=",.2f",
        margin=dict(l=10, r=10, t=30, b=10),
        height=600,
    )

    st.plotly_chart(fig, use_container_width=True)

    # === Tabela de conferência (opcional, para leigos) ===
    st.subheader("◆ Tabela - Somatório por Projeto")
    st.dataframe(
        soma_projeto[["Projetos", "Total"]].style.format({"Total": "{:,.2f}"}),
        use_container_width=True,
        height=450
    )

    with st.expander("❔ Como interpretar?"):
        st.markdown(
            "- **Cada barra** representa o **total** do valor da folha acumulado para aquele **projeto** "
            "nos anos selecionados.\n"
            "- Use os **filtros** de Ano e de nome para focar nos projetos de interesse.\n"
        )