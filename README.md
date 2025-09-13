# 📊 Data Analysis UPE

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38.0-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Dashboards interativos em **Streamlit** com dados **JSON** para dois domínios:
- **PROPEGI Financeiro**
- **Projeto de Desenvolvimento Tecnológico**

Projetado para **gestão baseada em dados** no contexto profissional e universitário, com foco em clareza, comparabilidade e replicabilidade.



## 🚀 Tecnologias
- Python 3.10+
- Streamlit
- Pandas
- Plotly


## 📂 Estrutura do Repositório
```
DATA-ANALYSIS-UPE/
│── images/
│   └── upeLogo.png
│
│── Projeto de Desenvolvimento Tecnologico/
│   ├── input/
│   │   └── Projetos de Desenvolvimento Tecnologico.json
│   └── Streamlit/
│       ├── analisesFinanceiras/
│       │   ├── analise1.py
│       │   ├── analise2.py
│       │   ├── analise3.py
│       │   ├── analise4.py
│       │   └── data_utils.py
│       └── projeto_tecnologico.py
│
│── PROPEGI Financeiro/
│   ├── input/
│   │   └── Financas.json
│   └── Streamlit/
│       ├── analisesFinanceiras/
│       │   ├── analise1_comparativa.py
│       │   ├── analise2_somatorio.py
│       │   ├── analise3_total_mensal.py
│       │   └── data_utils.py
│       └── projeto_financeiro.py
│
│── .streamlit/
│   └── config.toml
│── requirements.txt
│── requirements-dev.txt
│── Makefile
│── tasks.py
│── .gitignore
└── README.md
```



## ⚙️ Instalação

### 1) Clone
```bash
git clone https://github.com/seu-usuario/DATA-ANALYSIS-UPE.git
cd DATA-ANALYSIS-UPE
```

### 2) Ambiente virtual
```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

### 3) Dependências
```bash
# Produção
pip install -r requirements.txt

# Desenvolvimento (opcional)
pip install -r requirements-dev.txt
```

## ▶️ Execução Rápida

### Via **Makefile** (Linux/Mac; Windows com Make instalado)
```bash
make run-financeiro
make run-tecnologico
```

### Via **Invoke** (Windows/Linux/Mac – sem Make)
```bash
# já dentro do venv:
invoke run-financeiro
invoke run-tecnologico
```

### Comando Streamlit direto
```bash
streamlit run "PROPEGI Financeiro/Streamlit/projeto_financeiro.py"
streamlit run "Projeto de Desenvolvimento Tecnologico/Streamlit/projeto_tecnologico.py"
```

> 💡 Dica: no topo de cada app, utilize:
> ```python
> import streamlit as st
> st.set_page_config(
>     page_title="Data Analysis UPE",
>     page_icon="images/upeLogo.png",
>     layout="wide"
> )
> ```


## 🔎 O que cada análise faz (explicado de forma explícita)

### 📁 PROPEGI Financeiro (`PROPEGI Financeiro/Streamlit/analisesFinanceiras/`)

1) **`analise1_comparativa.py` — Heatmap comparativo (projeto × mês × ano)**
- **Objetivo:** comparar visualmente a **intensidade de valores de folha** por **projeto** ao longo dos **meses** e **anos**.
- **Como ler:** tons mais escuros indicam meses com maior valor; permite detectar **sazonalidade**, **picos** e **meses críticos** por projeto.
- **Uso típico:** priorização de orçamento e identificação de períodos de maior despesa.

2) **`analise2_somatorio.py` — Somatório por projeto (barras horizontais)**
- **Objetivo:** calcular o **total acumulado** (soma) por **projeto** em todo o período.
- **Como ler:** ranking claro de projetos por **custo total**; barras horizontais facilitam a leitura de nomes longos.
- **Uso típico:** comparações diretas entre projetos e definição de **TOP-N**.

3) **`analise3_total_mensal.py` — Total por mês (todas as iniciativas)**
- **Objetivo:** consolidar o **valor mensal total** somando **todos os projetos** por mês.
- **Como ler:** gráfico de barras verticais mostra **tendência temporal** do gasto agregado.
- **Uso típico:** visão macro para planejamento mensal e análise de **variação ao longo do tempo**.

> **Observação:** `data_utils.py` concentra funções de leitura/validação do JSON, tratamento de datas (mês/ano), agregações e formatação para os gráficos.

---

### 📁 Projeto de Desenvolvimento Tecnológico (`Projeto de Desenvolvimento Tecnologico/Streamlit/analisesFinanceiras/`)

1) **`analise1.py` — Séries temporais + cards de KPIs**
- **Objetivo:** mostrar a **evolução temporal** de métricas-chave dos projetos (ex.: custo, entregas, status) e **cards** com indicadores (ex.: total do período, média por mês).
- **Como ler:** a curva mostra tendência; cards resumem **KPIs executivos**.

2) **`analise2.py` — Comparativo por categoria/eixo (barras/treemap)**
- **Objetivo:** comparar **categorias de projetos** (ex.: eixo temático, área, centro) pelo valor ou quantidade.
- **Como ler:** barras/treemap evidenciam **peso relativo** por grupo.

3) **`analise3.py` — Distribuição e outliers (boxplot/histogram)**
- **Objetivo:** entender a **distribuição** das métricas (ex.: valores por projeto) e detectar **outliers**.
- **Como ler:** boxplots mostram mediana, quartis e pontos fora do padrão.

4) **`analise4.py` — Tabela com filtros por coluna + export**
- **Objetivo:** prover uma **tabela interativa** com **filtros individuais por coluna** para exploração detalhada (projeto, período, status).
- **Como ler:** aplicar filtros combinados; opcionalmente exportar o subconjunto.

> **Observação:** `data_utils.py` padroniza campos do JSON, cria colunas derivadas (ex.: `ano`, `mes`) e agrega dados.

## ✅ Qualidade e Produtividade
- **Lint:** `flake8`
- **Formatação:** `black`
- **Testes:** `pytest`
- **Automação:** `Makefile` e `invoke (tasks.py)`

Comandos úteis:
```bash
# Com Make
make lint
make format
make test
make clean

# Com Invoke
invoke lint
invoke format
invoke test
invoke clean
```

## 🏫 Contexto Acadêmico
Projeto desenvolvido na **Universidade de Pernambuco (UPE)**, integrando **Engenharia de Software**, **Análise de Dados** e **Ciência de Dados** para apoiar **Decisões Gerenciais** baseadas em evidências.

## 👤 Autor
**Gabriel Lopes de Albuquerque** — UPE  
📧 [gabriel.lopes.albuquerque@gmail.com] · 🔗 LinkedIn: [https://www.linkedin.com/in/gabriel-lopes-de-albuquerque-658a8317b/]

## 📄 Licença
Distribuído sob a licença **MIT**. Consulte o arquivo `LICENSE`.
