# Streamlit/analisesFinanceiras/data_utils.py
import pandas as pd

# Caminho padrão (ajuste se necessário caso o JSON esteja em outro local)
DEFAULT_JSON_PATH = "../input/Projetos de Desenvolvimento Tecnologico.json"

BRL_COLS = ["Valor agência", "Valor unidade", "Valor IA-UPE"]

def carregar_json(caminho: str = DEFAULT_JSON_PATH) -> pd.DataFrame:
    """
    Lê o JSON diretamente (lista de objetos) e retorna um DataFrame.
    """
    df = pd.read_json(caminho)
    return df

def _br_to_float(serie: pd.Series) -> pd.Series:
    """
    Converte strings no formato brasileiro '1.234.567,89' para float 1234567.89.
    Aceita também números já numéricos.
    """
    if pd.api.types.is_numeric_dtype(serie):
        return serie.astype(float)
    serie = serie.fillna("0").astype(str).str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
    return pd.to_numeric(serie, errors="coerce").fillna(0.0)

def normalizar_valores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Garante que colunas monetárias estejam em float.
    """
    for c in BRL_COLS:
        if c in df.columns:
            df[c] = _br_to_float(df[c])
    return df

def preparar_datas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converte 'Data publicação' para datetime e cria colunas de ano/mês.
    """
    df = df.copy()
    df["Data publicação"] = pd.to_datetime(df["Data publicação"], dayfirst=True, errors="coerce")
    df["Ano"] = df["Data publicação"].dt.year
    df["Mes"] = df["Data publicação"].dt.month
    # Nome do mês com 2 dígitos para ordenar bem no gráfico/tabela
    df["MesNome"] = df["Data publicação"].dt.strftime("%m/%b")
    return df

def agrupar_mensal(df: pd.DataFrame, ano: int) -> pd.DataFrame:
    """
    Filtra pelo ano e soma por mês os valores da agência, unidade e IA-UPE.
    """
    df_ano = df[df["Ano"] == ano].copy()
    if df_ano.empty:
        # Cria um dataframe vazio com meses 01..12 para não quebrar o gráfico
        base = pd.DataFrame({"Mes": range(1, 13)})
        base["MesNome"] = base["Mes"].apply(lambda m: pd.Timestamp(year=ano, month=m, day=1).strftime("%m/%b"))
        for c in BRL_COLS:
            base[c] = 0.0
        return base

    grp = (
        df_ano.groupby(["Mes", "MesNome"], as_index=False)[BRL_COLS]
        .sum()
        .sort_values("Mes")
    )
    # Garante todos os meses (1..12) mesmo que faltem dados
    meses_completos = pd.DataFrame({"Mes": range(1, 12 + 1)})
    meses_completos["MesNome"] = meses_completos["Mes"].apply(
        lambda m: pd.Timestamp(year=ano, month=m, day=1).strftime("%m/%b")
    )
    out = meses_completos.merge(grp, on=["Mes", "MesNome"], how="left").fillna(0.0)
    return out

def kpis_anuais(df_mes: pd.DataFrame) -> dict:
    """
    Calcula os totais do ano (soma dos meses) para mostrar nos cards.
    """
    return {
        "agencia": float(df_mes["Valor agência"].sum()),
        "unidade": float(df_mes["Valor unidade"].sum()),
        "ia_upe": float(df_mes["Valor IA-UPE"].sum()),
    }
