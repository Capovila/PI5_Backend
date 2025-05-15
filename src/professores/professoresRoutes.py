import sys
import os
from flask import Blueprint, jsonify, request
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from supabase_client import supabase

professores_bp = Blueprint("professores", __name__, url_prefix="/professores")


@professores_bp.route("/", methods=["GET"])
def get_professores():
    try:
        response = supabase.table("professores").select("*").execute()
        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"})

@professores_bp.route("/<int:id>", methods=["GET"])
def get_professor_by_id(id):
    try:
        response = supabase.table("professores").select("*").eq("ra_professor", id).execute()
            
            # Verifica se o registro foi encontrado
        if not response.data:
            return jsonify({"error": "Registro não encontrado"}), 404
            
            # Retorna os dados do professor
        return jsonify(response.data[0])
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar registro"})
    

@professores_bp.route("/pagination", methods=["GET"])
def get_professor_pagination():
    try:
        data = request.json
        limit = data.get("limit", 10)  # Limite padrão de 10 registros
        page = data.get("page", 1)  # Página padrão é a 1ª

        # Calcula o intervalo de registros
        start = (page - 1) * limit
        end = start + limit - 1

        # Busca os registros no Supabase
        response = supabase.table("professores").select("*").range(start, end).execute()

        # Verifica se há registros
        if not response.data:
            return jsonify({"error": "Nenhum registro encontrado"}), 404

        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"}), 500


@professores_bp.route("/", methods=["POST"])
def add_professores():
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


        return jsonify({"message": "Registro inserido com sucesso"}), 201
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao inserir o registro"}), 500

@professores_bp.route("/<int:id>", methods=["DELETE"])
def delete_professor(id):
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
    

@professores_bp.route("/<int:id>", methods=["PUT"])
def patch_professor(id):
    try:
        data = request.json
        nome = data.get("nome")
        email = data.get("email")
        senha = data.get("senha")
        is_admin = data.get("is_admin")
        is_liberado = data.get("is_liberado")

        # Atualiza o registro no Supabase
        response = supabase.table("professores").update({
            "nome": nome,
            "email": email,
            "senha": senha,
            "is_admin": is_admin,
            "is_liberado": is_liberado
        }).eq("ra_professor", id).execute()

        # Verifica se o registro foi encontrado e atualizado
        if not response.data:
            return jsonify({"error": "Registro não encontrado"}), 404

        return jsonify({"message": "Registro atualizado com sucesso"}), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao atualizar o registro"}), 500
    

@professores_bp.route("/liberar/<int:id>", methods=["PUT"])
def liberar_professor(id):
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
    

@professores_bp.route("/admin/<int:id>", methods=["PUT"])
def professor_admin(id):
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