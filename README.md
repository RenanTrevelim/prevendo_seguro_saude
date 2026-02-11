# 💰 Previsão de Valor de Seguro de Saúde  
### Machine Learning com Scikit-Learn e Spark ML + Deploy com Streamlit

Este projeto demonstra a construção de modelos de regressão para previsão do valor de seguro de saúde utilizando duas abordagens distintas:

- ✅ **Scikit-Learn (ambiente local / single-machine)**
- ✅ **Spark MLlib (ambiente distribuído / Big Data)**

O modelo disponibilizado na aplicação web foi treinado com **Scikit-Learn** e posteriormente exportado para produção.

---

## 🎯 Objetivo

Prever o valor do seguro de saúde com base nas seguintes variáveis:

- Idade  
- IMC  
- Sexo  
- Número de filhos  
- Status de fumante  

---

## 🧠 Modelagem

### 🔹 1. Implementação com Scikit-Learn

- Tratamento e transformação de dados  
- Engenharia de variáveis  
- Aplicação de regressão  
- Avaliação de métricas  
- Serialização do modelo (`modelo.pkl`)  
- Modelo utilizado no deploy  

Notebook de treinamento:  
`ML_Treino_Regressão_Valor_Segura_de_Saúde.ipynb`

---

### 🔹 2. Implementação com Spark ML (PySpark)

- Criação de pipeline distribuído  
- Manipulação de dados em ambiente Spark  
- Treinamento de modelo de regressão utilizando MLlib  
- Comparação de desempenho  

Notebook Spark:  
`Spark - ML Regressão (valor seguro).ipynb`

---

## 🚀 Deploy da Aplicação

A aplicação foi desenvolvida em **Streamlit**, permitindo que o usuário insira dados e receba a previsão em tempo real.

Arquivo principal:  
`main.py`

### 🔄 Fluxo da aplicação:

1. Usuário insere dados no formulário  
2. Aplicação realiza transformação logarítmica das variáveis  
3. Modelo treinado com Scikit-Learn é carregado via `joblib`  
4. Previsão é realizada  
5. Resultado é convertido para escala original e exibido

<img width="717" height="586" alt="image" src="https://github.com/user-attachments/assets/db306db8-528b-4885-ba64-8060932e10d7" />
