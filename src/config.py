import os

class Config:
    # Caminho para a pasta onde o modelo será salvo/carregado
    MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'models_data')
    MODEL_FILENAME = 'modelo_previsao_media_turma.joblib'
    MODEL_FILEPATH = os.path.join(MODEL_DIR, MODEL_FILENAME)

    # Semente para reprodutibilidade na geração de fatores (se aplicável no service)
    RANDOM_SEED_ALUNO_FACTOR = 42
    RANDOM_SEED_TURMA_FACTOR = 123

    # Média padrão para alunos sem histórico ou disciplinas novas
    DEFAULT_HISTORICAL_AVG = 7.0
    DEFAULT_DISCIPLINE_AVG = 7.0 
