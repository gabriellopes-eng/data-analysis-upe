import streamlit as st
import plotly.express as px
import pandas as pd

from .data_utils import (
    carregar_json,
    preparar_datas,
    DEFAULT_JSON_PATH,
)

def run(caminho_json: str = DEFAULT_JSON_PATH):
    st.title(" ◈ Análise 2 — Projetos em desenvolvimento por segmento/ano")
    st.caption("Visualização da quantidade de projetos por segmento em cada ano.")

    # Carregamento 
    df = carregar_json(caminho_json)
    df = preparar_datas(df)

    # Verifica se a coluna "Segmento" existe
    if "Segmento" not in df.columns:
        st.error("A coluna 'Segmento' não foi encontrada no JSON.")
        st.stop()

    #  Agrupamento: Conta projetos por Ano e Segmento
    df_group = (
        df.groupby(["Ano", "Segmento"])
        .size()
        .reset_index(name="QtdProjetos")
        .sort_values(["Ano", "Segmento"])
    )

    # Gráfico de Barras Empilhadas 
    fig = px.bar(
        df_group,
        x="Ano",
        y="QtdProjetos",
        color="Segmento",
        text="QtdProjetos",
        title="❖ Projetos em desenvolvimento por segmento/ano",
        labels={"QtdProjetos": "Quantidade de Projetos"},
    )
    fig.update_layout(barmode="stack", xaxis=dict(type="category"))
    st.plotly_chart(fig, use_container_width=True)

    # Tabela
    with st.expander("◆ Ver tabela agregada"):
        st.dataframe(df_group, use_container_width=True)
