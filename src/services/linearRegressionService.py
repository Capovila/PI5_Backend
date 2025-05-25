import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.infrastructure.model_persistence_service import save_model_and_metrics, load_model_and_metrics
from src.config import Config
from src.infrastructure.supabase_client import supabase 

MODEL_DATA_CACHE = None

def _ensure_factors(df):
    df_copy = df.copy()
    if 'fator_aluno' not in df_copy.columns:
        np.random.seed(Config.RANDOM_SEED_ALUNO_FACTOR)
        fatores_aluno_map = {ra: np.random.normal(0, 0.5) for ra in df_copy['ra_aluno'].unique()}
        df_copy['fator_aluno'] = df_copy['ra_aluno'].map(fatores_aluno_map)
    if 'fator_turma' not in df_copy.columns:
        np.random.seed(Config.RANDOM_SEED_TURMA_FACTOR)
        fatores_turma_map = {turma: np.random.normal(0, 0.3) for turma in df_copy['id_turma'].unique()}
        df_copy['fator_turma'] = df_copy['id_turma'].map(fatores_turma_map)
    return df_copy

def train_linear_regression_model(df_historico_completo: pd.DataFrame):
    df_processed = _ensure_factors(df_historico_completo.copy())
    df_processed.sort_values(by=['ra_aluno', 'id_disciplina'], inplace=True)
    df_processed.loc[:, 'media_notas_anteriores_aluno'] = df_processed.groupby('ra_aluno')['nota'].transform(lambda x: x.expanding().mean().shift(1))
    df_processed.loc[:, 'media_notas_anteriores_aluno'] = df_processed['media_notas_anteriores_aluno'].fillna(Config.DEFAULT_HISTORICAL_AVG)
    df_processed.loc[:, 'media_geral_historica_disciplina'] = df_processed.groupby('id_disciplina')['nota'].transform('mean')

    df_agregado = df_processed.groupby(['id_turma', 'id_disciplina']).agg(
        media_real_notas_turma_disciplina=('nota', 'mean'),
        dificuldade_disciplina=('dificuldade', 'first'),
        media_do_historico_medio_alunos=('media_notas_anteriores_aluno', 'mean'),
        media_geral_historica_disciplina=('media_geral_historica_disciplina', 'first'),
        fator_turma_agregado=('fator_turma', 'first'),
        media_fator_aluno_turma=('fator_aluno', 'mean')
    ).reset_index()

    y_agregado = df_agregado['media_real_notas_turma_disciplina']
    X_agregado = df_agregado[[
        'dificuldade_disciplina', 'media_do_historico_medio_alunos',
        'media_geral_historica_disciplina', 'fator_turma_agregado',
        'media_fator_aluno_turma', 'id_turma'
    ]]

    X_train, X_test, y_train, y_test = train_test_split(X_agregado, y_agregado, test_size=0.2, random_state=42)

    colunas_numericas = ['dificuldade_disciplina', 'media_do_historico_medio_alunos',
                         'media_geral_historica_disciplina', 'fator_turma_agregado',
                         'media_fator_aluno_turma']
    colunas_categoricas = ['id_turma']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), colunas_numericas),
            ('cat', OneHotEncoder(handle_unknown='ignore', drop='first'), colunas_categoricas)
        ])

    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('regressor', LinearRegression())])
    
    pipeline.fit(X_train, y_train)
    y_pred_test = pipeline.predict(X_test)
    mae_teste = mean_absolute_error(y_test, y_pred_test)
    mse_teste = mean_squared_error(y_test, y_pred_test)
    rmse_teste = np.sqrt(mse_teste)
    r2_teste = r2_score(y_test, y_pred_test)

    modelo_e_metricas = {
        'pipeline': pipeline,
        'mae_teste': mae_teste,
        'rmse_teste': rmse_teste,
        'r2_teste': r2_teste
    }
    save_model_and_metrics(modelo_e_metricas)
    
    global MODEL_DATA_CACHE
    MODEL_DATA_CACHE = modelo_e_metricas
    
    return {"message": "Modelo treinado e salvo com sucesso.", "metrics": {"mae": mae_teste, "rmse": rmse_teste, "r2": r2_teste}}

def predict_average_grade_for_turma(id_turma_alvo: int, id_disciplina_futura: int, df_historico_completo: pd.DataFrame):
    global MODEL_DATA_CACHE
    if MODEL_DATA_CACHE is None:
        MODEL_DATA_CACHE = load_model_and_metrics() 

    if MODEL_DATA_CACHE is None or 'pipeline' not in MODEL_DATA_CACHE:
        return {"erro": "Modelo não está carregado ou é inválido. Por favor, treine o modelo primeiro."}

    pipeline = MODEL_DATA_CACHE['pipeline']
    metricas_modelo = {k: v for k, v in MODEL_DATA_CACHE.items() if k != 'pipeline'}

    try:
        response_disciplina = supabase.table('disciplinas').select('dificuldade').eq('id_disciplina', id_disciplina_futura).single().execute()
        
        if not response_disciplina.data:
            return {"erro": f"Disciplina com id {id_disciplina_futura} não encontrada no banco de dados."}
        
        dificuldade_disciplina_futura = response_disciplina.data.get('dificuldade')
        
        if dificuldade_disciplina_futura is None:
            return {"erro": f"Coluna 'dificuldade' não encontrada ou nula para a disciplina com id {id_disciplina_futura}."}

    except Exception as e:
        return {"erro": f"Erro ao buscar dados da disciplina {id_disciplina_futura}: {str(e)}"}

    df_processed_historico = _ensure_factors(df_historico_completo.copy())

    notas_da_disciplina_futura_no_historico = df_processed_historico[df_processed_historico['id_disciplina'] == id_disciplina_futura]['nota']
    media_geral_hist_disc_futura = notas_da_disciplina_futura_no_historico.mean() if not notas_da_disciplina_futura_no_historico.empty else Config.DEFAULT_DISCIPLINE_AVG

    alunos_da_turma_alvo = df_processed_historico[df_processed_historico['id_turma'] == id_turma_alvo]['ra_aluno'].unique()
    if len(alunos_da_turma_alvo) == 0:
         return {"erro": f"Nenhum aluno encontrado para a turma com id {id_turma_alvo}."}
    
    soma_medias_individuais = 0
    count_alunos_com_historico = 0
    for ra_aluno_turma in alunos_da_turma_alvo:
        historico_aluno_especifico = df_processed_historico[df_processed_historico['ra_aluno'] == ra_aluno_turma].sort_values(by='id_disciplina')
        media_aluno_para_previsao = historico_aluno_especifico['nota'].mean() if not historico_aluno_especifico.empty else Config.DEFAULT_HISTORICAL_AVG
        soma_medias_individuais += media_aluno_para_previsao
        count_alunos_com_historico +=1
    media_do_hist_medio_alunos_turma = (soma_medias_individuais / count_alunos_com_historico) if count_alunos_com_historico > 0 else Config.DEFAULT_HISTORICAL_AVG

    fator_turma_especifico = 0
    turma_data = df_processed_historico[df_processed_historico['id_turma'] == id_turma_alvo]
    if not turma_data.empty:
        fator_turma_especifico = turma_data['fator_turma'].iloc[0]
    
    media_fator_aluno_da_turma = 0
    if len(alunos_da_turma_alvo) > 0:
        fatores_alunos_turma_temp = df_processed_historico.loc[df_processed_historico['ra_aluno'].isin(alunos_da_turma_alvo), 'fator_aluno'].unique()
        if len(fatores_alunos_turma_temp) > 0:
             media_fator_aluno_da_turma = np.mean(fatores_alunos_turma_temp)

    dados_para_prever = pd.DataFrame({
        'dificuldade_disciplina': [dificuldade_disciplina_futura], 
        'media_do_historico_medio_alunos': [media_do_hist_medio_alunos_turma],
        'media_geral_historica_disciplina': [media_geral_hist_disc_futura],
        'fator_turma_agregado': [fator_turma_especifico],
        'media_fator_aluno_turma': [media_fator_aluno_da_turma],
        'id_turma': [id_turma_alvo]
    })
    
    media_prevista_turma = pipeline.predict(dados_para_prever)
    
    resposta = {
        "id_turma_prevista": id_turma_alvo,
        "id_disciplina_prevista": id_disciplina_futura,
        "dificuldade_utilizada": dificuldade_disciplina_futura,
        "media_prevista_para_turma": round(float(media_prevista_turma[0]), 2),
        "confiabilidade_modelo": {
            "erro_medio_absoluto_esperado_MAE": f"{metricas_modelo.get('mae_teste', 'N/A'):.4f}" if metricas_modelo.get('mae_teste') is not None else "N/A",
            "rmse_esperado": f"{metricas_modelo.get('rmse_teste', 'N/A'):.4f}" if metricas_modelo.get('rmse_teste') is not None else "N/A",
            "r2_esperado_0_a_1_maior_melhor": f"{metricas_modelo.get('r2_teste', 'N/A'):.4f}" if metricas_modelo.get('r2_teste') is not None else "N/A"
        }
    }
    return resposta
