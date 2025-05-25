import pandas as pd
from flask import Blueprint, jsonify, request
from src.services.LinearRegressionService import train_linear_regression_model, predict_average_grade_for_turma
from src.infrastructure.supabase_client import supabase 

class RegressaoLinearController:
    def __init__(self):
        self.regressao_linear_bp = Blueprint("regressaoLinear", __name__, url_prefix="/regressaoLinear")
        self._register_routes()

    def _register_routes(self):
        self.regressao_linear_bp.route("/treinar_modelo_media_turma", methods=["POST"])(self.train_model_endpoint) 
        self.regressao_linear_bp.route("/prever_media_disciplina_turma", methods=["POST"])(self.predict_model_endpoint)

    def train_model_endpoint(self):
        try:
            response = supabase.rpc('get_dataset_completo_para_treino').execute()
            
            if not response.data:
                return jsonify({"error": "Nenhum dado retornado do Supabase para treinamento."}), 500
            
            df_treino = pd.DataFrame(response.data)

            colunas_necessarias_treino = ['ra_aluno', 'id_disciplina', 'nota', 'id_turma', 'dificuldade', 'semestre', 'data_inicio_aluno']
            for col in colunas_necessarias_treino:
                if col not in df_treino.columns:
                    return jsonify({"error": f"Coluna '{col}' essencial para o treino não encontrada nos dados do Supabase. Verifique a RPC 'get_dataset_completo_para_treino'."}), 500

            resultado_treino = train_linear_regression_model(df_treino)
            return jsonify(resultado_treino), 200
        except Exception as err:
            import traceback
            tb_str = traceback.format_exc()
            return jsonify({"error": f"Erro ao treinar o modelo: {str(err)}", "traceback": tb_str}), 500

    def predict_model_endpoint(self):
        try:
            dados_requisicao = request.get_json()
            if not dados_requisicao or 'id_turma_alvo' not in dados_requisicao or 'id_disciplina_futura' not in dados_requisicao:
                return jsonify({"error": "Requisição JSON inválida. Forneça 'id_turma_alvo' (int) e 'id_disciplina_futura' (int)."}), 400

            id_turma_alvo = dados_requisicao['id_turma_alvo']
            id_disciplina_futura = dados_requisicao['id_disciplina_futura']

            if not isinstance(id_turma_alvo, int) or not isinstance(id_disciplina_futura, int):
                return jsonify({"error": "'id_turma_alvo' e 'id_disciplina_futura' devem ser números inteiros."}), 400

            response_historico = supabase.rpc('get_dataset_completo_para_treino').execute()
            if not response_historico.data:
                 return jsonify({"error": "Nenhum dado histórico encontrado no Supabase para fazer a previsão."}), 500
            
            df_historico_completo = pd.DataFrame(response_historico.data)

            colunas_necessarias_previsao = ['ra_aluno', 'id_disciplina', 'nota', 'id_turma'] 
            if 'dificuldade' not in df_historico_completo.columns:
                 colunas_necessarias_previsao.append('dificuldade')


            for col in colunas_necessarias_previsao:
                if col not in df_historico_completo.columns:
                    return jsonify({"error": f"Coluna '{col}' essencial para a previsão não encontrada nos dados históricos do Supabase. Verifique a RPC 'get_dataset_completo_para_treino'."}), 500


            resultado_previsao = predict_average_grade_for_turma(
                id_turma_alvo,
                id_disciplina_futura, 
                df_historico_completo
            )
            
            if "erro" in resultado_previsao: 
                status_code = 400  
                if "Modelo não está carregado" in resultado_previsao.get("erro","") or "Erro ao buscar dados da disciplina" in resultado_previsao.get("erro",""):
                    status_code = 500 
                return jsonify(resultado_previsao), status_code
            
            return jsonify(resultado_previsao), 200
        except Exception as err:
            import traceback
            tb_str = traceback.format_exc()
            return jsonify({"error": f"Erro ao fazer a previsão: {str(err)}", "traceback": tb_str}), 500
