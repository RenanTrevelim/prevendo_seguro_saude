import joblib
import pandas as pd
import xgboost as xgb

preprocessador = joblib.load("models/preprocessamento.pkl")
modelo = joblib.load("models/modelo_xgb.pkl")

COLUNAS_ENTRADA = ["idade", "imc", "sexo", "fumante", "regiao", "filhos"]

COLUNAS_FINAIS = [
    "idade",
    "imc",
    "sexo_male",
    "fumante_yes",
    "regiao_northwest",
    "regiao_southeast",
    "regiao_southwest",
    "filhos",
]

def predict(dados):
    """
    Realiza a predição a partir dos dados de entrada.

    Converte os dados em DataFrame, aplica o preprocessamento,
    transforma no formato esperado pelo modelo e retorna as previsões.

    Parâmetros
    ----------
    dados : dict ou list
        Dados de entrada com as features do modelo.

    Retorna
    -------
    numpy.ndarray
        Previsões do modelo.
    """
    df = pd.DataFrame(dados)
    df = df[COLUNAS_ENTRADA]

    df_transformado = preprocessador.transform(df)

    df_transformado = pd.DataFrame(df_transformado, columns=COLUNAS_FINAIS)

    dmatrix = xgb.DMatrix(df_transformado, feature_names=COLUNAS_FINAIS)

    previsao = modelo.predict(dmatrix)
    return previsao