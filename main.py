import pandas as pd
import plotly.express as px
import streamlit as st

# Carrega os dados do CSV
def carregar_dados():
    dados = pd.read_csv("vendas_paises.csv")
    return dados

# Cria o gráfico animado
def criar_grafico(dados):
    grafico = px.bar(
        dados,
        x="Vendas",
        y="País",
        orientation="h",
        color="País",
        animation_frame="Ano",
        title="Vendas por País"
    )
    return grafico

# Título da página
st.title("Gráfico de Vendas por País")

# Carrega os dados
dados = carregar_dados()

# Filtros na barra lateral
anos = sorted(dados["Ano"].unique())
paises = sorted(dados["País"].unique())

anos_selecionados = st.sidebar.multiselect("Escolha os anos:", anos, default=anos)
paises_selecionados = st.sidebar.multiselect("Escolha os países:", paises, default=paises)

# Filtra os dados
dados_filtrados = dados[
    (dados["Ano"].isin(anos_selecionados)) &
    (dados["País"].isin(paises_selecionados))
]

# Cria e mostra o gráfico
grafico = criar_grafico(dados_filtrados)
st.plotly_chart(grafico)
