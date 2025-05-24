import sys
import os
from flask import Blueprint, jsonify, request

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from supabase_client import supabase

class DisciplinaController:
    def __init__(self):
        self.disciplinas_bp = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")
        self._register_routes()

    def _register_routes(self):
        self.disciplinas_bp.route("/", methods=["GET"])(self.get_disciplinas)
        self.disciplinas_bp.route("/area/<string:area_relacionada>", methods=["GET"])(self.get_disciplinas_by_area)
        self.disciplinas_bp.route("/pagination", methods=["GET"])(self.get_disciplinas_pagination)
        self.disciplinas_bp.route("/semestre/<int:semestre>", methods=["GET"])(self.get_disciplinas_by_semestre)
        self.disciplinas_bp.route("/<int:id>", methods=["GET"])(self.get_disciplina_by_id)
        self.disciplinas_bp.route("/professor/<int:ra>", methods=["GET"])(self.get_disciplinas_by_professor_ra)
        self.disciplinas_bp.route("/", methods=["POST"])(self.add_disciplina)
        self.disciplinas_bp.route("/importar_csv", methods=["POST"])(self.add_disciplinas_from_csv)
        self.disciplinas_bp.route("/<int:id>", methods=["DELETE"])(self.delete_disciplina)
        self.disciplinas_bp.route("/<int:id>", methods=["PUT"])(self.update_disciplina)

    def get_disciplinas(self):
        try:
            response = supabase.table("disciplinas").select("*").execute()
            return jsonify(response.data)
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"})


    def get_disciplinas_by_area(area_relacionada):
        try:

            # Busca as disciplinas no Supabase com base na área relacionada
            response = supabase.table("disciplinas").select("*").eq("area_relacionada", area_relacionada).execute()

            # Verifica se há registros
            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            return jsonify(response.data), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"}), 500

    def get_disciplinas_pagination(self):
        try:
            data = request.json
            limit = data.get("limit", 10)  # Limite padrão de 10 registros
            page = data.get("page", 1)  # Página padrão é a 1ª

            # Calcula o intervalo de registros
            start = (page - 1) * limit
            end = start + limit - 1

            # Busca os registros no Supabase
            response = supabase.table("disciplinas").select("*").range(start, end).execute()

            # Verifica se há registros
            if not response.data:
                return jsonify({"error": "Nenhum registro encontrado"}), 404

            return jsonify(response.data), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"}), 500

    def get_disciplinas_by_semestre(self, semestre):
        try:
            # Busca as disciplinas no Supabase com base no semestre
            response = supabase.table("disciplinas").select("*").eq("semestre", semestre).execute()

            # Verifica se há registros
            if not response.data:
                return jsonify({"error": "Nenhum registro encontrado"}), 404

            return jsonify(response.data), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"}), 500

    def get_disciplina_by_id(self, id):
        try:
            # Busca a disciplina no Supabase com base no ID
            response = supabase.table("disciplinas").select("*").eq("id_disciplina", id).execute()

            # Verifica se o registro foi encontrado
            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            return jsonify(response.data[0]), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"}), 500

    def get_disciplinas_by_professor_ra(self, ra):
        try:
            # Busca as disciplinas no Supabase com base no RA do professor
            response = supabase.table("disciplinas").select("*").eq("ra_professor", ra).execute()

            # Verifica se há registros
            if not response.data:
                return jsonify({"error": "Nenhum registro encontrado"}), 404

            return jsonify(response.data), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"}), 500

    def add_disciplina(self):
        try:
            data = request.json
            nome = data.get("nome")
            descricao = data.get("descricao")
            teor_programacao = data.get("teor_programacao")
            teor_matematica = data.get("teor_matematica")
            teor_testes = data.get("teor_testes")
            teor_banco_dados = data.get("teor_banco_dados")
            teor_frontend = data.get("teor_frontend")
            teor_backend = data.get("teor_backend")
            teor_requisitos = data.get("teor_requisitos")
            teor_ux = data.get("teor_ux")
            teor_gestao = data.get("teor_gestao")
            semestre = data.get("semestre")
            ra_professor = data.get("ra_professor")

            # Verifica se os campos obrigatórios foram fornecidos
            if not nome or not teor_programacao or not teor_matematica or not teor_testes or not teor_banco_dados or not teor_frontend or not teor_backend or not teor_requisitos or not teor_ux or not teor_gestao or not semestre or not ra_professor:
                return jsonify({"error": "Campos obrigatórios não fornecidos"}), 400

            # Insere o registro no Supabase
            response = supabase.table("disciplinas").insert({
                "nome": nome,
                "descricao": descricao,
                "teor_programacao": teor_programacao,
                "teor_matematica": teor_matematica,
                "teor_testes": teor_testes,
                "teor_banco_dados": teor_banco_dados,
                "teor_frontend": teor_frontend,
                "teor_backend": teor_backend,
                "teor_requisitos": teor_requisitos,
                "teor_ux": teor_ux,
                "teor_gestao": teor_gestao,
                "semestre": semestre,
                "ra_professor": ra_professor
            }).execute()

            # Verifica se a inserção foi bem-sucedida
            if not response.data:
                return jsonify({"error": "Erro ao inserir o registro"}), 400

            return jsonify({"message": "Disciplina inserida com sucesso"}), 201
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao inserir a disciplina"}), 500

    def add_disciplinas_from_csv(self):
        try:
            payload = request.json
            csv_data = payload.get("data")
            print("CSV Data:", csv_data)

            if not csv_data:
                return jsonify({"error": "Nenhum dado fornecido."}), 400

            disciplinas_formatadas = []
            for linha in csv_data:
                try:
                    disciplina = {
                        "nome": linha["nome"],
                        "descricao": linha["descricao"],
                        "teor_programacao": float(linha["teor_programacao"]),
                        "teor_matematica": float(linha["teor_matematica"]),
                        "teor_testes": float(linha["teor_testes"]),
                        "teor_banco_dados": float(linha["teor_banco_dados"]),
                        "teor_frontend": float(linha["teor_frontend"]),
                        "teor_backend": float(linha["teor_backend"]),
                        "teor_requisitos": float(linha["teor_requisitos"]),
                        "teor_ux": float(linha["teor_ux"]),
                        "teor_gestao": float(linha["teor_gestao"]),
                        "semestre": int(linha["semestre"]),
                        "ra_professor": int(linha["ra_professor"])
                    }
                    disciplinas_formatadas.append(disciplina)
                except (KeyError, ValueError) as e:
                    print(f"Erro ao processar linha: {linha}, erro: {e}")
                    continue

            if not disciplinas_formatadas:
                return jsonify({"error": "Nenhum registro válido para importar."}), 400

            response = supabase.table("disciplinas").insert(disciplinas_formatadas).execute()

            return jsonify({
                "message": f"{len(disciplinas_formatadas)} disciplinas inseridos com sucesso.",
                "data": response.data
            }), 201

        except Exception as err:
            print("Erro ao importar disciplinas via CSV:", err)
            return {"error": str(err)}, 500

    def delete_disciplina(self, id):
        try:
            # Deleta a disciplina no Supabase com base no ID
            response = supabase.table("disciplinas").delete().eq("id_disciplina", id).execute()

            # Verifica se o registro foi encontrado e deletado
            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            return jsonify({"message": "Disciplina deletada com sucesso"}), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao deletar a disciplina"}), 500

    def update_disciplina(self, id):
        try:
            data = request.json
            nome = data.get("nome")
            descricao = data.get("descricao")
            teor_programacao = data.get("teor_programacao")
            teor_matematica = data.get("teor_matematica")
            teor_testes = data.get("teor_testes")
            teor_banco_dados = data.get("teor_banco_dados")
            teor_frontend = data.get("teor_frontend")
            teor_backend = data.get("teor_backend")
            teor_requisitos = data.get("teor_requisitos")
            teor_ux = data.get("teor_ux")
            teor_gestao = data.get("teor_gestao")
            semestre = data.get("semestre")
            ra_professor = data.get("ra_professor")

            # Verifica se os campos obrigatórios foram fornecidos
            if not nome or not teor_programacao or not teor_matematica or not teor_testes or not teor_banco_dados or not teor_frontend or not teor_backend or not teor_requisitos or not teor_ux or not teor_gestao or not semestre or not ra_professor:
                return jsonify({"error": "Campos obrigatórios não fornecidos"}), 400

            # Atualiza o registro no Supabase
            response = supabase.table("disciplinas").update({
                "nome": nome,
                "descricao": descricao,
                "teor_programacao": teor_programacao,
                "teor_matematica": teor_matematica,
                "teor_testes": teor_testes,
                "teor_banco_dados": teor_banco_dados,
                "teor_frontend": teor_frontend,
                "teor_backend": teor_backend,
                "teor_requisitos": teor_requisitos,
                "teor_ux": teor_ux,
                "teor_gestao": teor_gestao,
                "semestre": semestre,
                "ra_professor": ra_professor
            }).eq("id_disciplina", id).execute()

            # Verifica se o registro foi encontrado e atualizado
            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            return jsonify({"message": "Disciplina atualizada com sucesso"}), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao atualizar a disciplina"}), 500