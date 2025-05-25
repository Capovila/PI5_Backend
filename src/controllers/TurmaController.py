import sys
import os
from flask import Blueprint, jsonify, request

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.infrastructure.supabase_client import supabase

class TurmaController:
    def __init__(self):
        self.turmas_bp = Blueprint("turmas", __name__, url_prefix="/turmas")
        self._register_routes()

    def _register_routes(self):
        self.turmas_bp.route("/", methods=["GET"])(self.get_turmas)
        self.turmas_bp.route("/data", methods=["GET"])(self.get_turmas_by_date)
        self.turmas_bp.route("/<int:id>", methods=["GET"])(self.get_turma_by_id)
        self.turmas_bp.route("/pagination", methods=["GET"])(self.get_turmas_pagination)
        self.turmas_bp.route("/", methods=["POST"])(self.add_turmas)
        self.turmas_bp.route("/importar_csv", methods=["POST"])(self.add_turmas_from_csv)
        self.turmas_bp.route("/<int:id>", methods=["DELETE"])(self.delete_turma)
        self.turmas_bp.route("/<int:id>", methods=["PUT"])(self.update_turma)
        self.turmas_bp.route("/graduar/<int:id>", methods=["PUT"])(self.update_turma_status_to_graduate)

    def get_turmas(self):
        try:
            response = supabase.table("turmas").select("*").execute()
            return jsonify(response.data)
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"})


    def get_turmas_by_date(self):
        try:
            data_inicio = request.json.get("data_inicio")

            response = supabase.table("turmas").select("*").eq("data_inicio", data_inicio).execute()

            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            return jsonify(response.data), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"}), 500


    def get_turma_by_id(self, id): # Corrected method name
        try:
            response = supabase.table("turmas").select("*").eq("id_turma", id).execute()

            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            return jsonify(response.data[0])
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar registro"})


    def get_turmas_pagination(self):
        try:
            data = request.json
            limit = data.get("limit", 10)
            page = data.get("page", 1)

            start = (page - 1) * limit
            end = start + limit - 1

            response = supabase.table("turmas").select("*").range(start, end).execute()

            if not response.data:
                return jsonify({"error": "Nenhum registro encontrado"}), 404

            return jsonify(response.data), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"}), 500


    def add_turmas(self):
        try:
            data = request.json
            data_inicio = data.get("data_inicio")
            isgraduated = data.get("isgraduated", False)

            response = supabase.table("turmas").insert({
                "data_inicio": data_inicio,
                "isgraduated": isgraduated
            }).execute()

            if not response.data:
                return jsonify({"error": "Erro ao inserir o registro"}), 400

            return jsonify({"message": "Turma inserida com sucesso"}), 201
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao inserir a turma"}), 500


    def add_turmas_from_csv(self):
        try:
            payload = request.json
            csv_data = payload.get("data")
            print("CSV Data:", csv_data)

            if not csv_data:
                return jsonify({"error": "Nenhum dado fornecido."}), 400

            turmas_formatadas = []
            for linha in csv_data:
                try:
                    turma = {
                        "data_inicio": linha["data_inicio"],
                        "isgraduated": linha.get("isgraduated", False)
                    }
                    turmas_formatadas.append(turma)
                except KeyError as e:
                    print(f"Erro ao processar linha: {linha}, erro: {e}")
                    continue

            if not turmas_formatadas:
                return jsonify({"error": "Nenhum registro válido para importar."}), 400

            response = supabase.table("turmas").insert(turmas_formatadas).execute()

            return jsonify({
                "message": f"{len(turmas_formatadas)} turmas inseridas com sucesso.",
                "data": response.data
            }), 201

        except Exception as err:
            print("Erro ao importar turmas via CSV:", err)
            return {"error": str(err)}, 500


    def delete_turma(self, id): # Corrected method name
        try:
            response = supabase.table("turmas").delete().eq("id_turma", id).execute()

            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            return jsonify({"message": "Registro deletado com sucesso"}), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao deletar o registro"}), 500


    def update_turma(self, id):
        try:
            data = request.json
            data_inicio = data.get("data_inicio")
            isgraduated = data.get("isgraduated")

            update_data = {}
            if data_inicio is not None:
                update_data["data_inicio"] = data_inicio
            if isgraduated is not None:
                update_data["isgraduated"] = isgraduated

            if not update_data:
                return jsonify({"error": "Nenhum dado para atualizar fornecido"}), 400

            response = supabase.table("turmas").update(update_data).eq("id_turma", id).execute()

            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            return jsonify({"message": "Turma atualizada com sucesso"}), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao atualizar a turma"}), 500


    def update_turma_status_to_graduate(self, id):
        try:
            response = supabase.table("turmas").update({
                "isgraduated": True
            }).eq("id_turma", id).execute()

            if not response.data:
                return jsonify({"error": "Registro não encontrado"}), 404

            return jsonify({"message": "Turma graduada com sucesso"}), 200
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao graduar a turma"}), 500