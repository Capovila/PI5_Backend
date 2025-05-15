import sys
import os
from flask import Blueprint, jsonify, request
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from supabase_client import supabase

turma_disciplina_bp = Blueprint("turmaDisciplina", __name__, url_prefix="/turmaDisciplina")

@turma_disciplina_bp.route("/", methods=["GET"])
def get_turma_disciplina():
    try:
        response = supabase.table("turma_disciplina").select("*").execute()
        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"}), 500

@turma_disciplina_bp.route("/<int:id>", methods=["GET"])
def get_turma_disciplina_by_id(id):
    try:
        response = supabase.table("turma_disciplina").select("*").eq("id_turma_disciplina", id).execute()
        if not response.data:
            return jsonify({"error": "Registro nao encontrado"}), 404
        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar registro"}), 500

@turma_disciplina_bp.route("/turma/<int:id>", methods=["GET"])
def get_disciplina_by_turma_id(id):
    try:
        response = supabase.table("turma_disciplina").select("*").eq("id_turma", id).execute()
        if not response.data:
            return jsonify({"error": "Registro nao encontrado"}), 404
        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar registro"}), 500

@turma_disciplina_bp.route("/disciplina/<int:id>", methods=["GET"])
def get_turmas_by_disciplina_id(id):
    try:
        response = supabase.table("turma_disciplina").select("*").eq("id_disciplina", id).execute()
        if not response.data:
            return jsonify({"error": "Registro nao encontrado"}), 404
        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar registro"}), 500

@turma_disciplina_bp.route("/", methods=["POST"])
def add_turma_disciplina():
    try:
        data = request.json
        id_turma = data.get("id_turma")
        id_disciplina = data.get("id_disciplina")
        taxa_aprovacao = data.get("taxa_aprovacao")
        is_concluida = data.get("is_concluida")

        response = supabase.table("turma_disciplina").insert([{
            "id_turma": id_turma,
            "id_disciplina": id_disciplina,
            "taxa_aprovacao": taxa_aprovacao if is_concluida else None,
            "is_concluida": is_concluida
        }]).execute()

        if not response.data:
            return jsonify({"error": "Erro ao inserir registro"}), 400

        return jsonify({"message": "Registro inserido com sucesso", "data": response.data}), 201
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao inserir registro"}), 500

@turma_disciplina_bp.route("/<int:id>", methods=["DELETE"])
def delete_turma_disciplina(id):
    try:
        response = supabase.table("turma_disciplina").delete().eq("id_turma_disciplina", id).execute()
        if not response.data:
            return jsonify({"error": "Registro nao encontrado"}), 404
        return jsonify({"message": "Registro deletado com sucesso"})
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao apagar registro"}), 500

@turma_disciplina_bp.route("/<int:id>", methods=["PUT"])
def patch_turma_disciplina(id):
    try:
        data = request.json
        id_turma = data.get("id_turma")
        id_disciplina = data.get("id_disciplina")
        taxa_aprovacao = data.get("taxa_aprovacao")
        is_concluida = data.get("is_concluida")

        print(data)

        update_fields = {}
        if id_turma is not None:
            update_fields["id_turma"] = id_turma
        if id_disciplina is not None:
            update_fields["id_disciplina"] = id_disciplina
        if is_concluida is not None:
            update_fields["is_concluida"] = is_concluida
        update_fields["taxa_aprovacao"] = taxa_aprovacao
        

        response = supabase.table("turma_disciplina").update(update_fields).eq("id_turma_disciplina", id).execute()
        if not response.data:
            return jsonify({"error": "Registro nao encontrado"}), 404
        return jsonify({"message": "Registro atualizado com sucesso"})
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao atualizar registro"}), 500

@turma_disciplina_bp.route("/concluir/<int:id>", methods=["PUT"])
def concluir_disciplina(id):
    try:
        response = supabase.table("turma_disciplina").update({"is_concluida": True}).eq("id_turma_disciplina", id).execute()
        if not response.data:
            return jsonify({"error": "Registro nao encontrado"}), 404
        return jsonify({"message": "Disciplina concluída com sucesso"})
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao concluir disciplina"}), 500

