import streamlit as st
import numpy as np
import pandas as pd
import joblib
import xgboost as xgb

st.set_page_config(
    page_title='Previsão de Seguro de Saúde',
    layout='centered',
)

st.title('Previsão de Seguro de Saúde')

# Importando o modelo de ML treinado
modelo = joblib.load('modelo.pkl')

# Inserindo as informações do usuário
sexo = st.selectbox('Sexo:', options=['Masculino', 'Feminino'])
sexo = 1 if sexo =='Masculino' else 0

filhos = st.number_input('Número de Filhos:', min_value=0, max_value=5, value=0, step=1)

fumante = st.selectbox('É Fumante?', options=['Sim', 'Não'])
fumante = 1 if fumante =='Sim' else 0

log_idade = st.number_input('Idade :', min_value=18.0, max_value=100.0, value=18.0, step=1.0)

log_imc = st.number_input('IMC :', min_value=10.0, max_value=50.0, value=10.0, step=1.0)

# Botão para enviar os dados e fazer a previsão
enviar = st.button('Prever Custo do Seguro')


if enviar:
    if filhos == '' or log_idade == '' or log_imc == '':
        st.warning('Por favor, preencha todos os campos antes de enviar.')
    else:

        entrada_df = pd.DataFrame([{
                        "sexo": sexo,
                        "filhos": filhos,
                        "fumante": fumante,
                        "log_idade": np.log(log_idade),
                        "log_imc": np.log(log_imc),
                    }])

        dm = xgb.DMatrix(entrada_df)

        previsao = modelo.predict(dm)

        st.write(f'O valor previsto do seguro de saúde é: R$ {np.exp(previsao[0]):.2f}')