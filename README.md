# 💰 Previsão de Valor de Seguro de Saúde  
### Machine Learning com Scikit-Learn e Spark ML + Deploy com Streamlit

Este projeto apresenta a construção e comparação de modelos de regressão para previsão do valor de seguro de saúde, utilizando duas abordagens distintas:

- ✅ **Scikit-Learn (ambiente local / single-machine)**
- ✅ **Spark MLlib (ambiente distribuído / Big Data)**

O modelo disponibilizado na aplicação web foi treinado com **Scikit-Learn** e exportado para produção.

---

## 📌 Contexto do Problema

A precificação de seguros de saúde depende de fatores individuais como idade, IMC e hábitos de risco. Modelos preditivos auxiliam na estimativa de valores mais justos e na análise de risco.

Este projeto simula um cenário real de precificação baseada em variáveis demográficas e comportamentais.

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
- Codificação de variáveis categóricas  
- Transformação logarítmica da variável alvo  
- Treinamento de modelo de regressão  
- Avaliação com métricas (R², MAE, RMSE)  
- Serialização do modelo (`modelo.pkl`)  
- Modelo utilizado no deploy  

📓 Notebook de treinamento:  
`ML_Treino_Regressão_Valor_Segura_de_Saúde.ipynb`

---

### 🔹 2. Implementação com Spark ML (PySpark)

- Criação de pipeline distribuído  
- Manipulação de dados em ambiente Spark  
- Treinamento com MLlib  
- Comparação de desempenho com abordagem local  

📓 Notebook Spark:  
`Spark - ML Regressão (valor seguro).ipynb`

---

## 📊 Resultados

*(Valores utilizando Função Logarítmica)*

**Modelo Scikit-Learn - XGBoost:**

- R²: 0.87  
- RMSE: 0.43  
- MAE: 0.19  

A aplicação da transformação logarítmica reduziu a heterocedasticidade e melhorou a estabilidade do modelo.

---

## 🚀 Deploy da Aplicação

A aplicação foi desenvolvida em **Streamlit**, permitindo que o usuário insira dados e receba a previsão em tempo real.

Arquivo principal:  
`main.py`

### 🔄 Fluxo da aplicação

1. Usuário insere dados no formulário  
2. Aplicação realiza transformação logarítmica das variáveis  
3. Modelo treinado com Scikit-Learn é carregado via `joblib`  
4. Previsão é realizada  
5. Resultado é convertido para escala original e exibido  

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar a aplicação

```bash
streamlit run main.py
```

---

## 🏗 Diferenciais Técnicos

- Comparação entre ambiente single-machine e distribuído  
- Aplicação de transformação logarítmica para estabilização da variância  
- Pipeline completo: tratamento → treino → avaliação → serialização → deploy  
- Estrutura preparada para escalabilidade  

---

## 🛠 Stack Tecnológica

<div>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white">
  <img src="https://img.shields.io/badge/PySpark-FF9900?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
</div>

---

## 📷 Preview da Aplicação

<img width="717" height="586" alt="Preview da aplicação" src="https://github.com/user-attachments/assets/db306db8-528b-4885-ba64-8060932e10d7" />
