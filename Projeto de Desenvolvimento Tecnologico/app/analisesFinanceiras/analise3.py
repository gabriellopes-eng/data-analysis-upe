import streamlit as st
import plotly.express as px
import numpy as np

from .data_utils import (
    carregar_json,
    normalizar_valores,
    preparar_datas,
    DEFAULT_JSON_PATH,
)

#  Utils de exibição
def _brl(v: float) -> str:
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def _inject_css():
    st.markdown(
        """
        <style>
          .kpi-card {
            background: #111418;
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 14px;
            padding: 16px 18px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.25);
          }
          .kpi-title { font-size: 0.92rem; color: #c9d1d9; margin-bottom: 6px; }
          .kpi-big   { font-size: 1.75rem; font-weight: 700; margin-bottom: 8px; line-height: 1.2; }
          .kpi-small { font-size: 0.85rem; color: #9aa4af; }
          .kpi-small span { color: #c9d1d9; font-weight: 600; }
        </style>
        """,
        unsafe_allow_html=True,
    )

def kpi_card(title: str, big_value: str, small_label: str, small_value: str):
    st.markdown(
        f"""
        <div class="kpi-card">
          <div class="kpi-title">{title}</div>
          <div class="kpi-big">{big_value}</div>
          <div class="kpi-small"><span>{small_label}</span> {small_value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------- Página ----------------
def run(caminho_json: str = DEFAULT_JSON_PATH):
    st.title("◈ Análise 3 — Recebimentos anuais por órgão (Agência, Unidade, IA-UPE)")
    st.caption("Comparativo de quanto cada órgão recebeu em cada ano.")

    # --- Carregamento ---
    df = carregar_json(caminho_json)
    df = normalizar_valores(df)
    df = preparar_datas(df)

    # --- Agrupamento por Ano ---
    df_group = (
        df.groupby("Ano")[["Valor agência", "Valor unidade", "Valor IA-UPE"]]
        .sum()
        .reset_index()
        .sort_values("Ano")
    )

    # --- Gráfico ---
    fig = px.bar(
        df_group,
        x="Ano",
        y=["Valor agência", "Valor unidade", "Valor IA-UPE"],
        barmode="group",
        text_auto=".2s",
        title="❖ Recebimentos anuais por órgão",
        labels={"value": "R$ total no ano", "variable": "Órgão"},
    )
    fig.update_layout(xaxis=dict(type="category"))
    st.plotly_chart(fig, use_container_width=True)

    # --- Cards resumo ---
    _inject_css()
    st.subheader("❖ Resumo dos anos")

    tot_agencia = float(df_group["Valor agência"].sum())
    tot_unidade = float(df_group["Valor unidade"].sum())
    tot_iaupe   = float(df_group["Valor IA-UPE"].sum())

    # Identifica o ano com maior soma total
    df_group["TotalAno"] = df_group["Valor agência"] + df_group["Valor unidade"] + df_group["Valor IA-UPE"]
    idx_pico   = df_group["TotalAno"].idxmax()
    ano_pico   = int(df_group.loc[idx_pico, "Ano"])
    valor_pico = float(df_group.loc[idx_pico, "TotalAno"])

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        kpi_card("Total acumulado — Agência", _brl(tot_agencia), "Período completo:", f"{df_group['Ano'].min()}–{df_group['Ano'].max()}")
    with c2:
        kpi_card("Total acumulado — Unidade", _brl(tot_unidade), "Período completo:", f"{df_group['Ano'].min()}–{df_group['Ano'].max()}")
    with c3:
        kpi_card("Total acumulado — IA-UPE", _brl(tot_iaupe), "Período completo:", f"{df_group['Ano'].min()}–{df_group['Ano'].max()}")
    with c4:
        kpi_card(f"Ano pico — {ano_pico}", _brl(valor_pico), "Maior soma entre órgãos:", "Soma dos 3 valores")

    # --- Tabela ---
    st.markdown("---")
    with st.expander("◆ Ver tabela agregada"):
        st.dataframe(df_group, use_container_width=True)
