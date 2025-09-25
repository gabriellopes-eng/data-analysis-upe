import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from .data_utils import carregar_financas_json, filtrar

DEFAULT_JSON_PATH = Path(__file__).resolve().parents[2] / "input" / "Financas.json"

def run():
    st.header("◈ Comparativo de Valores das Folhas por Projeto com base no Mês e o Ano")

    # Config de Entrada (Caminho do meu arquivo JSON) 
    caminho = st.text_input(
        "Caminho do Financas.json",
        value=str(DEFAULT_JSON_PATH),
        help="Altere caso seu arquivo esteja em outro local."
    )

    # Carrega os meus Dados
    try:
        df = carregar_financas_json(caminho)
    except Exception as e:
        st.error(f"Erro ao carregar JSON: {e}") 
        return

    # Filtros 
    anos_unicos = sorted(df["Ano"].unique().tolist())
    projetos_unicos = sorted(df["Projetos"].unique().tolist())

    col_f1, col_f2, col_f3 = st.columns([1, 2, 1])
    with col_f1:
        anos_sel = st.multiselect("Filtrar por Ano (opcional)", anos_unicos, default=anos_unicos)
    with col_f2:
        projetos_sel = st.multiselect("Filtrar por Projetos (opcional)", projetos_unicos)
    with col_f3:
        if st.button("Limpar filtros"):
            anos_sel = anos_unicos
            projetos_sel = []

    df_filt = filtrar(df, anos_sel, projetos_sel)

    if df_filt.empty:
        st.warning("Sem dados para os filtros escolhidos.")
        return

    # --- Pivot para Heatmap: linhas = Projetos; colunas = AnoMes; valores = soma da folha ---
    # Ordena colunas por 'ord_col' (Ano*100 + Número do mês) para manter sequência Jan..Dez
    ord_cols = (
        df_filt[["AnoMes", "ord_col"]]
        .drop_duplicates()
        .sort_values("ord_col")
    )
    ordem_colunas = ord_cols["AnoMes"].tolist()

    tabela = (
        df_filt
        .groupby(["Projetos", "AnoMes"], as_index=False)["Valor da folha"]
        .sum()
        .pivot(index="Projetos", columns="AnoMes", values="Valor da folha")
        .reindex(columns=ordem_colunas)
        .fillna(0.0)
    )

    # Formatação amigável para hover (R$ 12.345,67)
    # Plotly aceita hovertemplate; px.imshow facilita o heatmap
    fig = px.imshow(
        tabela.values,
        labels=dict(x="Mês/Ano", y="Projetos", color="R$"),
        x=tabela.columns,
        y=tabela.index,
        aspect="auto",
        color_continuous_scale="Blues"
    )
    fig.update_traces(
        hovertemplate="Projeto: %{y}<br>Mês/Ano: %{x}<br>Valor: R$ %{z:,.2f}<extra></extra>"
    )
    fig.update_coloraxes(colorbar_title="Valor (R$)")

    st.plotly_chart(fig, use_container_width=True)

    #  Dicas simples 
    with st.expander("❔ Como ler este gráfico?"):
        st.markdown(
            "- **Cada célula** representa a **soma** do valor da folha daquele **Projeto** naquele **Mês/Ano**.\n"
            "- **Azul mais escuro** = valor maior; **mais claro** = valor menor.\n"
            "- Use os **filtros** acima para focar em anos ou projetos específicos.\n"
        )

    # Tabela abaixo para conferência usando a biblioteca pandas (dataframe)
    st.subheader("◆ Tabela Resumida")
    st.dataframe(
        tabela.style.format("{:,.2f}"),
        use_container_width=True,
        height=400
    )
