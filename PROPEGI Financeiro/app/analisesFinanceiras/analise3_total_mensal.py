# Streamlit/AnalisesFinanceiros/analise3_total_mensal.py
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from .data_utils import carregar_financas_json, filtrar

DEFAULT_JSON_PATH = Path(__file__).resolve().parents[2] / "input" / "Financas.json"

def run():
    st.header("◈ Análise 3: Evolução Mensal do Valor Total das Folhas por Projeto")

    # Entrada do caminho do JSON 
    caminho = st.text_input(
        "Caminho do Financas.json",
        value=str(DEFAULT_JSON_PATH),
        help="Se necessário, ajuste para o local onde o arquivo está."
    )

    # === Carregar dados com tratamentos simples ===
    try:
        df = carregar_financas_json(caminho)
    except Exception as e:
        st.error(f"Erro ao carregar JSON: {e}")
        return

    # === Filtros simples ===
    anos_disponiveis = sorted(df["Ano"].unique().tolist())
    anos_sel = st.multiselect("Filtrar por Ano (opcional)", anos_disponiveis, default=anos_disponiveis)

    df_filt = filtrar(df, anos_sel, None)
    if df_filt.empty:
        st.warning("Sem dados para os filtros escolhidos.")
        return

    # Agregação: soma por AnoMes (todos os projetos) 
    # Mantém ordem natural de tempo usando 'ord_col' (Ano*100 + Número do mês)
    ordem = (
        df_filt[["AnoMes", "ord_col"]]
        .drop_duplicates()
        .sort_values("ord_col")
    )
    ordem_cols = ordem["AnoMes"].tolist()

    total_mensal = (
        df_filt.groupby("AnoMes", as_index=False)["Valor da folha"]
        .sum()
        .rename(columns={"Valor da folha": "Total"})
        .merge(ordem, on="AnoMes", how="left")
        .sort_values("ord_col")
    )

    # === Gráfico: Barras Verticais ===
    fig = px.bar(
        total_mensal,
        x="AnoMes",
        y="Total",
        text="Total",
        labels={"AnoMes": "Mês/Ano", "Total": "Total (R$)"},
    )
    fig.update_traces(
        texttemplate="R$ %{y:,.2f}",
        hovertemplate="Mês/Ano: %{x}<br>Total (todos os projetos): R$ %{y:,.2f}<extra></extra>"
    )
    fig.update_layout(
        xaxis_title="Mês/Ano",
        yaxis_title="Total (R$)",
        xaxis_tickangle=-45,
        yaxis_tickformat=",.2f",
        margin=dict(l=10, r=10, t=30, b=10),
        height=600,
    )

    st.plotly_chart(fig, use_container_width=True)

    # === Tabela para conferência (opcional) ===
    st.subheader("◆ Tabela - Total Mensal (Todos os projetos)")
    st.dataframe(
        total_mensal[["AnoMes", "Total"]].style.format({"Total": "{:,.2f}"}),
        use_container_width=True,
        height=450
    )

    with st.expander("❔ Como interpretar?"): # Dica simples para visualização
        st.markdown(
            "- **Cada barra** representa o **total da folha** somando **todos os projetos** naquele **Mês/Ano**.\n"
            "- Use o **filtro de Ano** para focar em períodos específicos.\n"
            "- Dica: se quiser comparar meses iguais de anos diferentes (ex.: Jan/2021 vs Jan/2022), "
            "mantenha mais de um ano selecionado e observe as barras correspondentes no eixo X."
        )