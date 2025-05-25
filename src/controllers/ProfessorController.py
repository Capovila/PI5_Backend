import sys
import os
from flask import Blueprint, jsonify, request

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.infrastructure.supabase_client import supabase

class ProfessorController:
    def __init__(self):
        self.professores_bp = Blueprint("professores", __name__, url_prefix="/professores")
        self._register_routes()

    def _register_routes(self):
        self.professores_bp.route("/", methods=["GET"])(self.get_professores)
        self.professores_bp.route("/<int:id>", methods=["GET"])(self.get_professor_by_id)
        self.professores_bp.route("/pagination", methods=["GET"])(self.get_professor_pagination)
        self.professores_bp.route("/", methods=["POST"])(self.add_professores)
        self.professores_bp.route("/importar_csv", methods=["POST"])(self.add_professores_from_csv)
        self.professores_bp.route("/<int:id>", methods=["DELETE"])(self.delete_professor)
        self.professores_bp.route("/<int:id>", methods=["PUT"])(self.update_professor)
        self.professores_bp.route("/liberar/<int:id>", methods=["PUT"])(self.update_professor_status_to_liberado)
        self.professores_bp.route("/admin/<int:id>", methods=["PUT"])(self.update_professor_to_admin)

    def get_professores(self):
        try:
            response = supabase.table("professores").select("*").execute()
            return jsonify(response.data)
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"}), 500

    def get_professor_by_id(self, id):
        try:
            response = supabase.table("professores").select("*").eq("ra_professor", id).execute()

            # Verifica se o registro foi encontrado
            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            # Retorna os dados do professor (o primeiro item da lista, pois eq deve retornar apenas um)
            return jsonify(response.data[0])
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar registro"}), 500

    def get_professor_pagination(self):
        try:
            data = request.json
            limit = data.get("limit", 10)  # Limite padrão de 10 registros
            page = data.get("page", 1)  # Página padrão é a 1ª

            # Calcula o intervalo de registros para a paginação
            start = (page - 1) * limit
            end = start + limit - 1

            # Busca os registros no Supabase usando o método range para paginação
            response = supabase.table("professores").select("*").range(start, end).execute()

            # Verifica se há registros
            if not response.data:
                return jsonify({"error": "Nenhum registro encontrado"}), 404

            return jsonify(response.data), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"}), 500

    def add_professores(self):
        try:
            data = request.json
            ra_professor = data.get("ra_professor")
            nome = data.get("nome")
            email = data.get("email")
            senha = data.get("senha")
            is_admin = data.get("is_admin", False)  # Valor padrão: False
            is_liberado = data.get("is_liberado", False)  # Valor padrão: False

            # Insere o registro no Supabase
            response = supabase.table("professores").insert({
                "ra_professor": ra_professor,
                "nome": nome,
                "email": email,
                "senha": senha,
                "is_admin": is_admin,
                "is_liberado": is_liberado
            }).execute()

            # Retorna uma mensagem de sucesso
            return jsonify({"message": "Registro inserido com sucesso"}), 201
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao inserir o registro"}), 500

    def add_professores_from_csv(self):
        try:
            payload = request.json
            csv_data = payload.get("data")
            print("CSV Data:", csv_data)

            if not csv_data:
                return jsonify({"error": "Nenhum dado fornecido."}), 400

            professores_formatados = []
            for linha in csv_data:
                try:
                    # Formata cada linha do CSV para o formato esperado pelo Supabase
                    professor = {
                        "ra_professor": int(linha["ra_professor"]),
                        "nome": linha["nome"],
                        "email": linha["email"],
                        "senha": "123456",  # Senha padrão para importação CSV
                        "is_admin": False,  # Status padrão para importação CSV
                        "is_liberado": True  # Status padrão para importação CSV
                    }
                    professores_formatados.append(professor)
                except (KeyError, ValueError) as e:
                    # Imprime erro para linhas malformadas e continua processando as outras
                    print(f"Erro ao processar linha: {linha}, erro: {e}")
                    continue

            if not professores_formatados:
                return jsonify({"error": "Nenhum registro válido para importar."}), 400

            # Insere todos os professores formatados no Supabase
            response = supabase.table("professores").insert(professores_formatados).execute()

            return jsonify({
                "message": f"{len(professores_formatados)} professores inseridos com sucesso.",
                "data": response.data
            }), 201

        except Exception as err:
            print("Erro ao importar professores via CSV:", err)
            return jsonify({"error": str(err)}), 500

    def delete_professor(self, id):
        try:
            # Deleta o registro no Supabase
            response = supabase.table("professores").delete().eq("ra_professor", id).execute()

            # Verifica se o registro foi encontrado e deletado
            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            return jsonify({"message": "Registro deletado com sucesso"}), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao deletar o registro"}), 500

    def update_professor(self, id):
        try:
            data = request.json
            nome = data.get("nome")
            email = data.get("email")
            senha = data.get("senha")
            is_admin = data.get("is_admin")
            is_liberado = data.get("is_liberado")

            # Cria um dicionário com os dados a serem atualizados, ignorando None
            update_data = {k: v for k, v in {
                "nome": nome,
                "email": email,
                "senha": senha,
                "is_admin": is_admin,
                "is_liberado": is_liberado
            }.items() if v is not None}

            if not update_data:
                return jsonify({"error": "Nenhum dado para atualizar fornecido"}), 400

            # Atualiza o registro no Supabase
            response = supabase.table("professores").update(update_data).eq("ra_professor", id).execute()

            # Verifica se o registro foi encontrado e atualizado
            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            return jsonify({"message": "Registro atualizado com sucesso"}), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao atualizar o registro"}), 500

    def update_professor_status_to_liberado(self, id):
        try:
            # Atualiza o campo `is_liberado` para `True`
            response = supabase.table("professores").update({
                "is_liberado": True
            }).eq("ra_professor", id).execute()

            # Verifica se o registro foi encontrado e atualizado
            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            return jsonify({"message": "Professor liberado com sucesso"}), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao liberar o professor"}), 500

    def update_professor_to_admin(self, id):
        try:
            # Busca o status atual de `is_admin`
            current_status = supabase.table("professores").select("is_admin").eq("ra_professor", id).execute()

            if not current_status.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            # Alterna o valor de `is_admin`
            new_status = not current_status.data[0]["is_admin"]

            # Atualiza o campo `is_admin`
            response = supabase.table("professores").update({
                "is_admin": new_status
            }).eq("ra_professor", id).execute()

            # Verifica se o registro foi atualizado
            if not response.data:
                return jsonify({"error": "Erro ao atualizar o registro"}), 400

            message = "Professor promovido a admin" if new_status else "Professor removido de admin"
            return jsonify({"message": message}), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao atualizar o status de admin"}), 500