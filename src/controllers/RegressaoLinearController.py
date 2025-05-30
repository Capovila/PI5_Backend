import pandas as pd
from flask import Blueprint, jsonify, request
import traceback

from src.services.linearRegressionService import train_linear_regression_model, predict_grades_and_approval_rate
from src.infrastructure.supabase_client import supabase 

class RegressaoLinearController:
    def __init__(self):
        self.regressao_linear_bp = Blueprint("regressaoLinear", __name__, url_prefix="/regressaoLinear")
        self._register_routes()

    def _register_routes(self):
        self.regressao_linear_bp.route("/treinar_modelo_nota", methods=["POST"])(self.train_model_endpoint) 
        self.regressao_linear_bp.route("/prever_desempenho_turma", methods=["POST"])(self.predict_model_endpoint)

    def train_model_endpoint(self):
        """
        Endpoint para treinar o modelo de regressão que prevê a nota dos alunos.
        """
        try:
            response = supabase.rpc('get_dataset_completo_para_treino').execute()
            
            if not response.data:
                return jsonify({"error": "Nenhum dado retornado do Supabase para treinamento."}), 500
            
            df_treino = pd.DataFrame(response.data)

            colunas_necessarias = ['ra_aluno', 'id_disciplina', 'nota', 'id_turma', 'dificuldade', 'semestre']
            for col in colunas_necessarias:
                if col not in df_treino.columns:
                    return jsonify({"error": f"Coluna essencial '{col}' não encontrada nos dados. Verifique a RPC 'get_dataset_completo_para_treino'."}), 500

            resultado_treino = train_linear_regression_model(df_treino)
            if "error" in resultado_treino:
                return jsonify(resultado_treino), 400
            
            return jsonify(resultado_treino), 200

        except Exception as err:
            tb_str = traceback.format_exc()
            return jsonify({"error": f"Erro crítico ao treinar o modelo: {str(err)}", "traceback": tb_str}), 500

    def predict_model_endpoint(self):
        """
        Endpoint que prevê a média da nota E a taxa de aprovação de uma turma
        para uma disciplina futura.
        """
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
                return jsonify({
                    "status": "previsao_indisponivel",
                    "mensagem": "Não há dados históricos para os alunos desta turma.",
                    "resultado_previsao": None
                }), 200
            
            df_historico_completo = pd.DataFrame(response_historico.data)

            resultado_previsao = predict_grades_and_approval_rate(
                id_turma_alvo,
                id_disciplina_futura, 
                df_historico_completo
            )
            
            if "erro" in resultado_previsao: 
                return jsonify({
                    "status": "previsao_indisponivel",
                    "mensagem": "Não há dados históricos para os alunos desta turma.",
                    "resultado_previsao": None
                }), 200
            
            return jsonify({
                    "status": "sucesso",
                    "mensagem": "Previsão feita com sucesso para os aulunos desta turma.",
                    "resultado_previsao": resultado_previsao
                }), 200
            
        except Exception as err:
            tb_str = traceback.format_exc()
            # Adicione prints para ver o erro no console do Flask
            print(f"==== ERRO CRÍTICO NA PREVISÃO ====")
            print(f"ID Turma Alvo: {dados_requisicao.get('id_turma_alvo', 'N/A')}") # Adiciona contexto
            print(f"ID Disciplina Futura: {dados_requisicao.get('id_disciplina_futura', 'N/A')}") # Adiciona contexto
            print(tb_str) # Imprime o traceback completo
            print(f"===================================")
            return jsonify({
                "status": "erro_servidor", # Melhor enviar um status claro para o frontend
                "mensagem": f"Erro crítico interno ao processar a previsão: {str(err)}",
                "detalhes": tb_str # Opcional, mas útil para depuração no frontend se você quiser
            }), 500