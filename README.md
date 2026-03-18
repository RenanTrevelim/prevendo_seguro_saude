# 💰 Previsão de Valor de Seguro de Saúde  
### Machine Learning com Scikit-Learn, XGBoost, Spark ML e Deploy com Streamlit

Este projeto apresenta um fluxo completo de análise de dados e modelagem preditiva para estimar o valor de seguros de saúde, passando por:

- 🔍 Análise Exploratória de Dados (EDA)  
- 🤖 Modelagem com Scikit-Learn e XGBoost  
- ⚡ Implementação com Spark ML (Big Data)  
- 🚀 Deploy de aplicação interativa com Streamlit  

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
- Região  

---

## 🔍 1. Análise Exploratória de Dados (EDA)

Nesta etapa foram realizadas:

- Análise de distribuição das variáveis  
- Identificação de assimetria nos dados  
- Avaliação de correlação entre variáveis  
- Detecção de outliers  

📓 Notebook:  
`Valor_Seguro_de_Saúde_EDA.ipynb`

### 🔎 Insights principais

- A variável `valor_seguro` apresenta alta assimetria  
- **Fumantes possuem valores significativamente mais elevados**  
- **Idade é uma das variáveis com maior impacto no aumento do custo**  
- IMC também contribui, mas com menor influência comparado a idade e tabagismo  

Diante disso, foi aplicada uma **transformação logarítmica na variável alvo**, visando melhorar o comportamento da distribuição para modelagem.

---

## 🧠 2. Modelagem com Machine Learning

### 🔹 Abordagem com Scikit-Learn + XGBoost

Etapas realizadas:

- Separação entre variáveis explicativas (X) e variável alvo (y)  
- Aplicação de transformação logarítmica na variável alvo  
- Engenharia e preparação das variáveis  
- Treinamento do modelo utilizando **XGBoost**  
- Avaliação com métricas de regressão (R², RMSE, MAE)  

📓 Notebook:  
`ML_Regressão_Valor_Seguro_de_Saúde.ipynb`

---

### 🔹 Pipeline de Pré-processamento

Foi construída uma pipeline responsável por padronizar os dados antes da modelagem:

- Transformação logarítmica das variáveis numéricas (`idade`, `imc`)  
- Codificação de variáveis categóricas (`sexo`, `fumante`, `regiao`) utilizando One-Hot Encoding  
- Garantia de consistência na estrutura dos dados de entrada  

Essa pipeline permite reutilizar exatamente o mesmo tratamento aplicado no treino durante a predição.

---

### 🔹 Treinamento e Salvamento do Modelo

Após o preprocessamento:

1. Os dados transformados foram utilizados para treinar o modelo XGBoost  
2. O modelo foi ajustado para aprender a relação entre as variáveis e o valor do seguro  
3. Tanto o preprocessamento quanto o modelo foram serializados para uso em produção  

Arquivos gerados:

- `models/preprocessamento.pkl`  
- `models/modelo_xgb.pkl`  

---

### 🔹 Abordagem com Spark ML (PySpark)

Também foi implementada uma versão utilizando Spark para simular ambiente de dados em larga escala:

- Criação de pipeline distribuído  
- Manipulação de dados em Spark  
- Treinamento com MLlib  
- Comparação com modelo local  

📓 Notebook:  
`Spark - ML Regressão (valor seguro).ipynb`

---

## 📊 Resultados

*(Valores com variável alvo em escala logarítmica)*

**Modelo XGBoost:**

- R²: 0.88  
- RMSE: 0.32 
- MAE: 0.18  


---

## ⚙️ 3. Pipeline de Produção

O fluxo de predição foi estruturado da seguinte forma:

1. Recebimento de dados brutos do usuário  
2. Aplicação do preprocessamento (`preprocessamento.pkl`)  
3. Conversão para formato `DMatrix`  
4. Predição com modelo XGBoost (`modelo_xgb.pkl`)  
5. Aplicação da função `exp()` para retornar ao valor original  

---

## 🚀 4. Deploy com Streamlit

A aplicação permite que o usuário insira os dados e visualize a previsão em tempo real.

Arquivo principal:

`main.py`

### 🔄 Fluxo da aplicação

1. Usuário preenche formulário  
2. Dados são enviados para a função de predição  
3. Pipeline transforma os dados  
4. Modelo realiza a previsão  
5. Resultado é exibido ao usuário  

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

- Pipeline completo de ML (EDA → Modelagem → Deploy)  
- Separação entre preprocessamento e modelo  
- Uso de XGBoost com DMatrix  
- Aplicação de transformação logarítmica  
- Integração com Streamlit  
- Comparação entre ambiente local e distribuído (Spark)  

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

<img width="720" height="652" alt="image" src="https://github.com/user-attachments/assets/7db1c2c9-68ff-473d-8cb4-48db236dbcf4" />

