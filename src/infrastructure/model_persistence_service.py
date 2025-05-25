import joblib
import os
from src.config import Config

def save_model_and_metrics(data_to_save):
    """
    Salva o pipeline do modelo e suas métricas em um arquivo.
    :param data_to_save: Dicionário contendo 'pipeline' e métricas como 'mae_teste'.
    """
    os.makedirs(Config.MODEL_DIR, exist_ok=True) 
    joblib.dump(data_to_save, Config.MODEL_FILEPATH)

def load_model_and_metrics():
    """
    Carrega o pipeline do modelo e suas métricas de um arquivo.
    Retorna um dicionário com 'pipeline' e métricas, ou None se o arquivo não existir.
    """
    if not os.path.exists(Config.MODEL_FILEPATH):
        return None
    
    try:
        loaded_data = joblib.load(Config.MODEL_FILEPATH)
        return loaded_data
    except Exception as e:
        return None

