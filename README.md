# ◈ Data Analysis UPE

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38.0-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Dashboards interativos em **Streamlit** com dados **JSON** para dois domínios:
- **PROPEGI Financeiro**
- **Projeto de Desenvolvimento Tecnológico**

Projetado para **gestão baseada em dados** no contexto profissional e universitário, com foco em clareza, comparabilidade e replicabilidade.

<img width="1536" height="1024" alt="63ad614e-5fd4-42e0-aebd-a09f11bfe0c4" src="https://github.com/user-attachments/assets/d3b19fe7-8477-4ae3-aa4c-f54d2c81dd9f" />




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


## 📁 Projeto de Desenvolvimento Tecnológico  
`Projeto de Desenvolvimento Tecnologico/Streamlit/analisesFinanceiras/`

### 1) Séries — **Recebimentos mensais por órgão (Agência, Unidade, IA-UPE)**
**Arquivo:** `analise1.py`  

- **Objetivo:** visualizar a **evolução mensal** dos recebimentos por **órgão** ao longo de um ano.
- **Como ler:** cada linha representa um órgão (Agência, Unidade, IA-UPE). Picos e vales indicam **sazonalidade** e **meses críticos**.
- **Filtros/controles:** seleção de **ano** (dropdown).
- **Uso típico:** detectar meses de maior entrada, comparar o comportamento entre órgãos e planejar **alocação/execução** mensal.

<img width="1365" height="533" alt="image" src="https://github.com/user-attachments/assets/672143ed-e281-45dc-a367-90f9df67b70d" />

---

### 2) Barras empilhadas — **Projetos em desenvolvimento por segmento/ano**
**Arquivo:** `analise2.py`  

- **Objetivo:** comparar a **quantidade de projetos** por **segmento** (Educação, Meio Ambiente, Saúde, Segurança, Tecnologia) em cada **ano**.
- **Como ler:** barras empilhadas por ano; cada cor é um segmento com o respectivo **rótulo de contagem**.
- **Filtros/controles:** visual agregado por ano (sem filtro adicional na imagem).
- **Uso típico:** priorização de portfólio por segmento; acompanhar **mudança de foco** ao longo dos anos.

<img width="1365" height="532" alt="image" src="https://github.com/user-attachments/assets/a8d0db67-8b90-456a-8af8-86a999e715b8" />

---

### 3) Barras agrupadas — **Recebimentos anuais por órgão (Agência, Unidade, IA-UPE)**
**Arquivo:** `analise3.py`  

- **Objetivo:** comparar o **total anual** recebido por cada **órgão**.
- **Como ler:** barras lado a lado (Agência, Unidade, IA-UPE) para cada ano; **rótulos** em k ajudam na leitura imediata.
- **Filtros/controles:** visão anual consolidada (sem filtro adicional na imagem).
- **Uso típico:** avaliação **macro** por órgão e ano; suporte a planejamento e **prestação de contas**.

<img width="1365" height="511" alt="image" src="https://github.com/user-attachments/assets/95e38bc6-57e6-40c9-85b1-a44c3b730e10" />

---

### 4) Barras + Donut — **Recebimentos por ano por Setor (Segmento)**
**Arquivo:** `analise4.py`  

- **Objetivo:** entender valores por **segmento** ao longo dos anos e a **distribuição percentual** em um **ano** específico.
- **Como ler:**  
  - **Barras** com valores por segmento em cada ano.  
  - **Donut** mostra a **participação (%)** de cada segmento no ano filtrado.
- **Filtros/controles:** seleção de **período/ano** (dropdown para a donut).
- **Uso típico:** balancear investimentos entre segmentos; identificar **concentrações** e **oportunidades**.

<img width="1365" height="522" alt="image" src="https://github.com/user-attachments/assets/7482dd2c-1d96-4bc4-91a5-93c83bf5706c" />
<img width="991" height="454" alt="image" src="https://github.com/user-attachments/assets/8eae47b1-defa-4d00-bdbd-c8df46626d6b" />

---

## 📁 PROPEGI Financeiro  
`PROPEGI Financeiro/Streamlit/analisesFinanceiras/`

### 1) Heatmap — **Comparativo de valores das folhas por projeto (Mês/Ano)**
**Arquivo:** `analise1_comparativa.py`  

- **Objetivo:** comparar a **intensidade mensal/anual** dos **valores de folha** por **projeto**.
- **Como ler:** tons mais escuros = **maior valor**; eixo Y são **projetos** e eixo X é **Mês/Ano**.
- **Filtros/controles:** **caminho do JSON**, filtro de **Ano (opcional)** e seleção de **projetos**; botão **Limpar filtros**.
- **Uso típico:** identificar **picos sazonais**, meses críticos por projeto e **lacunas** de execução.

<img width="1365" height="517" alt="image" src="https://github.com/user-attachments/assets/c0789844-83e2-4feb-935c-7a172b50572d" />

---

### 2) Barras horizontais — **Somatório dos valores das folhas por projeto**
**Arquivo:** `analise2_somatorio.py`  

- **Objetivo:** ranquear projetos pelo **total acumulado** (soma) no período filtrado.
- **Como ler:** barras ordenadas (desc); rótulos exibem o **total em R$** por projeto.
- **Filtros/controles:** filtro de **Ano (opcional)** e **busca por nome** do projeto (contém).
- **Uso típico:** definição de **TOP-N** de custo; priorização de auditoria e replanejamento.

<img width="1362" height="548" alt="image" src="https://github.com/user-attachments/assets/584bfb1e-9d7e-472d-a4eb-57a12941d8ca" />

---

### 3) Barras verticais — **Evolução mensal do valor total das folhas (todos os projetos)**
**Arquivo:** `analise3_total_mensal.py`  

- **Objetivo:** acompanhar o **total mensal** somando **todos os projetos**.
- **Como ler:** barras por mês; rótulos com valores em **R$** destacam picos e vales.
- **Filtros/controles:** filtro de **Ano (opcional)** e **projetos** (multi-seleção).
- **Uso típico:** visão **macro** para planejamento orçamentário e acompanhamento de **execução mensal**.

<img width="1365" height="519" alt="image" src="https://github.com/user-attachments/assets/5ca3284a-bdce-4d66-b7da-46180ccb4ce5" />


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
- 📘 Gmail: gabriel.lopes.albuquerque@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/gabriel-lopes-de-albuquerque-658a8317b/)

## 📄 Licença
Distribuído sob a licença **MIT**. Consulte o arquivo `LICENSE`.
