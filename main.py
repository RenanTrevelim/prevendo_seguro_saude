import streamlit as st
import numpy as np
from src.predict import predict

st.set_page_config(
    page_title="Previsão de Seguro de Saúde",
    layout="centered",
)

st.title("Previsão de Seguro de Saúde")

sexo_label = st.selectbox("Sexo:", options=["Masculino", "Feminino"])
filhos = st.number_input("Número de Filhos:", min_value=0, max_value=10, value=0, step=1)
fumante_label = st.selectbox("É fumante?", options=["Sim", "Não"])
idade = st.number_input("Idade:", min_value=18, max_value=100, value=18, step=1)
imc = st.number_input("IMC:", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
regiao = st.selectbox(
    "Região:",
    options=["southwest", "southeast", "northwest", "northeast"]
)

enviar = st.button("Prever custo do seguro")

if enviar:
    sexo = "male" if sexo_label == "Masculino" else "female"
    fumante = "yes" if fumante_label == "Sim" else "no"

    dados = [{
        "idade": idade,
        "imc": imc,
        "sexo": sexo,
        "fumante": fumante,
        "regiao": regiao,
        "filhos": filhos,
    }]

    previsao = predict(dados)
    valor_real = np.exp(previsao[0])

    st.success(f"Valor previsto do seguro: R$ {valor_real:.2f}")