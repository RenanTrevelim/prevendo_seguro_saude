# 💰 Previsão de Valor de Seguro de Saúde
### Machine Learning End-to-End com XGBoost, Spark e Deploy com Streamlit

Este projeto apresenta um pipeline completo de **Ciência de Dados**, desde a análise exploratória até o deploy de um modelo preditivo em produção.

🔗 O objetivo é estimar o valor de seguros de saúde com base em características individuais, simulando um cenário real de precificação.

---

## 🚀 Visão Geral do Projeto

O projeto cobre todas as etapas de um fluxo de Machine Learning:

- 🔍 Análise Exploratória de Dados (EDA)  
- 🧠 Modelagem preditiva com Scikit-Learn e XGBoost  
- ⚡ Processamento distribuído com Spark (PySpark)  
- 🚀 Deploy de aplicação interativa com Streamlit  

---

## 📌 Contexto do Problema

A precificação de seguros de saúde depende de fatores como idade, IMC e hábitos de risco. Modelos preditivos permitem:

- Estimar valores mais precisos  
- Avaliar risco de clientes  
- Apoiar decisões estratégicas  

Este projeto simula esse cenário utilizando dados demográficos e comportamentais.

---

## 🎯 Objetivo

Prever o valor do seguro (`charges`) com base nas variáveis:

- Idade  
- IMC  
- Sexo  
- Número de filhos  
- Status de fumante  
- Região  

---

## 🔍 Análise Exploratória de Dados (EDA)

A etapa de EDA teve como foco entender o comportamento dos dados e identificar padrões relevantes.

### Principais análises:
- Distribuição das variáveis  
- Correlação entre features  
- Identificação de outliers  
- Avaliação de assimetria  

📓 Notebook:  
`Valor_Seguro_de_Saúde_EDA.ipynb`

### 🔎 Principais insights

- A variável alvo apresenta **alta assimetria**  
- **Fumantes possuem custos significativamente maiores**  
- **Idade é um dos fatores mais relevantes**  
- IMC possui influência moderada  

📌 Foi aplicada uma **transformação logarítmica na variável alvo** para melhorar a modelagem.

---

## 🧠 Modelagem

### 🔹 Abordagem Principal (XGBoost)

Etapas:

- Preparação dos dados  
- Engenharia de features  
- Aplicação de transformação logarítmica  
- Treinamento com XGBoost  
- Avaliação com métricas de regressão  

📓 Notebook:  
`ML_Regressão_Valor_Seguro_de_Saúde.ipynb`

---

### 🔹 Pipeline de Pré-processamento

Foi criada uma pipeline para garantir consistência entre treino e produção:

- Transformação log em variáveis numéricas  
- One-Hot Encoding para variáveis categóricas  
- Padronização do formato de entrada  

---

### 🔹 Persistência do Modelo

Arquivos salvos para uso em produção:

- `models/preprocessamento.pkl`  
- `models/modelo_xgb.pkl`  

---

### ⚡ Versão com Spark (Big Data)

Implementação alternativa utilizando PySpark:

- Pipeline distribuído  
- Processamento em larga escala  
- Treinamento com MLlib  

📓 Notebook:  
`Spark - ML Regressão (valor seguro).ipynb`

---

## 📊 Resultados

*(com variável alvo em escala logarítmica)*

**XGBoost:**

- R²: **0.88**  
- RMSE: **0.32**  
- MAE: **0.18**  

---

## ⚙️ Pipeline de Produção

Fluxo de predição:

1. Entrada de dados do usuário  
2. Aplicação do preprocessamento  
3. Conversão para `DMatrix`  
4. Predição com XGBoost  
5. Inversão da transformação log (`exp`)  

---

## 🚀 Deploy com Streamlit

Aplicação interativa para previsão em tempo real.

📄 Arquivo principal:  
`main.py`

### 🔄 Fluxo da aplicação:

1. Usuário insere os dados  
2. Pipeline processa as informações  
3. Modelo gera a previsão  
4. Resultado é exibido na interface  

---


## ▶️ Como Executar o Projeto

### 🐳 Opção 1 — Docker (Recomendado)

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

### 2. Executar o Docker

```bash
docker build -t seguro-saude .
docker run -p 8501:8501 seguro-saude
```

### Opção 2 — Execução Local

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

### 2. Executar Local

```bash
pip install -r requirements.txt
streamlit run main.py
```


---
## 🏗 Diferenciais Técnicos

- Pipeline completo de Machine Learning (EDA → Modelagem → Deploy)  
- Separação entre etapa de preprocessamento e modelo preditivo  
- Uso de XGBoost com DMatrix para otimização de performance  
- Aplicação de transformação logarítmica na variável alvo  
- Deploy de aplicação interativa com Streamlit  
- Implementação adicional com Spark (processamento distribuído)  
- Ambiente reprodutível com Docker  

---

## 🛠 Stack Tecnológica

<div>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/XGBoost-EC6B23?style=for-the-badge">
  <img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white">
  <img src="https://img.shields.io/badge/PySpark-FF9900?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
</div>

---

## 📷 Preview da Aplicação

<img width="720" height="652" alt="image" src="https://github.com/user-attachments/assets/7db1c2c9-68ff-473d-8cb4-48db236dbcf4" />

