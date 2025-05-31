import pandas as pd
import numpy as np
import joblib
import os
import json

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler

MODEL_DIR = 'models_data'
os.makedirs(MODEL_DIR, exist_ok=True) 

MODEL_PATH = os.path.join(MODEL_DIR, 'modelo_previsao_media_turma.joblib')
SCALER_PATH = os.path.join(MODEL_DIR, 'scaler_nota.joblib')
COLUMNS_PATH = os.path.join(MODEL_DIR, 'model_columns_nota.joblib')
METRICS_PATH = os.path.join(MODEL_DIR, 'model_metrics.json')

NOTA_DE_CORTE_APROVACAO = 5.0  

def train_linear_regression_model(df: pd.DataFrame):
    """
    Treina um modelo de Regressão Linear para prever a 'nota', calcula as métricas
    de avaliação e salva todos os artefatos (modelo, scaler, colunas e métricas).
    """
    df['media_historica_aluno'] = df.groupby('ra_aluno')['nota'].transform('mean')
    df['media_dificuldade_aluno'] = df.groupby('ra_aluno')['dificuldade'].transform('mean')
    
    features = ['dificuldade', 'semestre', 'media_historica_aluno', 'media_dificuldade_aluno']
    target = 'nota'
    
    df_modelo = df[features + [target]].dropna()
    
    if len(df_modelo) < 50: 
        return {"error": "Dados insuficientes para treinar o modelo de forma confiável."}

    X = df_modelo[features]
    y = df_modelo[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    joblib.dump(features, COLUMNS_PATH)

    metrics_data = {
        "r2_score": r2,
        "mean_squared_error": mse,
        "mean_absolute_error": mae
    }
    with open(METRICS_PATH, 'w') as f:
        json.dump(metrics_data, f, indent=4)

    return {
        "message": "Modelo de Regressão Linear treinado e salvo com sucesso!",
        **metrics_data
    }


def predict_grades_and_approval_rate(id_turma_alvo: int, id_disciplina_futura: int, df_historico: pd.DataFrame):
    """
    Prevê as notas individuais dos alunos de uma turma, calcula a média geral e a
    taxa de aprovação prevista. Também inclui as métricas de qualidade do modelo utilizado.
    """
    if not all(os.path.exists(p) for p in [MODEL_PATH, SCALER_PATH, COLUMNS_PATH, METRICS_PATH]):
        return {"erro": "Modelo não está treinado ou arquivos essenciais não foram encontrados. Execute o endpoint de treino primeiro."}
    
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    model_columns = joblib.load(COLUMNS_PATH)
    with open(METRICS_PATH, 'r') as f:
        model_metrics = json.load(f)

    disciplina_futura_info_series = df_historico[df_historico['id_disciplina'] == id_disciplina_futura]
    if disciplina_futura_info_series.empty:
        return {"erro": f"Disciplina com id {id_disciplina_futura} não encontrada nos dados históricos."}
    disciplina_futura_info = disciplina_futura_info_series.iloc[0]
    
    dificuldade_futura = disciplina_futura_info['dificuldade']
    semestre_futuro = disciplina_futura_info['semestre']

    alunos_da_turma = df_historico[df_historico['id_turma'] == id_turma_alvo]['ra_aluno'].unique()
    if len(alunos_da_turma) == 0:
        return {"erro": f"Turma com id {id_turma_alvo} não encontrada ou não possui alunos."}

    dados_para_prever = []
    for ra in alunos_da_turma:
        hist_aluno = df_historico[df_historico['ra_aluno'] == ra]
        if not hist_aluno.empty:
            media_historica = hist_aluno['nota'].mean()
            media_dificuldade = hist_aluno['dificuldade'].mean()
            dados_para_prever.append({
                'dificuldade': dificuldade_futura, 'semestre': semestre_futuro,
                'media_historica_aluno': media_historica, 'media_dificuldade_aluno': media_dificuldade
            })

    if not dados_para_prever:
        return {"erro": "Não foi possível gerar features para os alunos da turma alvo."}
        
    df_para_prever = pd.DataFrame(dados_para_prever)[model_columns]
    
    X_para_prever_scaled = scaler.transform(df_para_prever)
    notas_previstas = model.predict(X_para_prever_scaled)
    notas_previstas = np.clip(notas_previstas, 0, 10)

    media_geral_prevista = np.mean(notas_previstas)
    alunos_aprovados = np.sum(notas_previstas >= NOTA_DE_CORTE_APROVACAO)
    total_alunos = len(notas_previstas)
    taxa_aprovacao = (alunos_aprovados / total_alunos) if total_alunos > 0 else 0

    return {
        "qualidade_do_modelo_utilizado": {
            "r2_score": round(model_metrics.get("r2_score", 0), 4),
            "erro_medio_absoluto_nota": f'{round(model_metrics.get("mean_absolute_error", 0), 2)}',
        },
        "previsao_de_desempenho": {
            "id_turma_alvo": id_turma_alvo,
            "id_disciplina_futura": id_disciplina_futura,
            "numero_de_alunos_considerados": total_alunos,
            "media_geral_prevista": round(media_geral_prevista, 2),
            "taxa_aprovacao_prevista": f"{taxa_aprovacao:.2%}"
        }
    }
