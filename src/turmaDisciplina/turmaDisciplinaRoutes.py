import sys
import os

import jwt
from flask import Blueprint, jsonify, request
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from supabase_client import supabase

turma_disciplina_bp = Blueprint("turmaDisciplina", __name__, url_prefix="/turmaDisciplina")

@turma_disciplina_bp.route("/", methods=["GET"])
def get_turma_disciplina():
    try:
        response = (
            supabase.table("turma_disciplina")
            .select(
                "id_turma_disciplina, id_turma, id_disciplina, taxa_aprovacao, is_concluida,"
                "disciplinas(id_disciplina, nome, descricao, semestre, area_relacionada, ra_professor)")
            .execute()
        )
        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"}), 500

@turma_disciplina_bp.route("/<int:id>", methods=["GET"])
def get_turma_disciplina_by_id(id):
    try:
        response = (
            supabase.table("turma_disciplina")
                .select(
                    "id_turma_disciplina, id_turma, id_disciplina, taxa_aprovacao, is_concluida,"
                    "disciplinas(id_disciplina, nome, descricao, semestre, area_relacionada, ra_professor)")
                .eq("id_turma_disciplina", id)
                .execute()
        )
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

@turma_disciplina_bp.route("/professor", methods=["GET"])
def get_turma_disciplina_by_professor_ra():
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({"error": "Erro ao autenticar"}), 401

    token_parts = auth_header.split()

    if len(token_parts) != 2 or token_parts[0].lower() != "bearer":
        return jsonify({"error": "Formato de token inválido"}), 401

    token = token_parts[1]

    try:
        SECRET_KEY = "tE91F+QWN88YeRb912YxdiBPIEdTWnEPBAwZOkt4PVGtdvevsMsVUT4PxzKOdTe8NmbEBfgz5NUa9CjZKCECfA=="
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"], audience="authenticated")

        email = payload["email"]

        # Executar a query para buscar o ra_professor
        result = (
            supabase.table("professores")
            .select("ra_professor")
            .eq("email", email)
            .execute()
        )

        if not result.data:
            return jsonify({"error": "Professor não encontrado"}), 404

        # ✅ Acessar o valor de ra_professor
        ra_professor = result.data[0]["ra_professor"]

        # ✅ Buscar os dados da turma_disciplina usando o ra_professor
        response = (
            supabase.table("turma_disciplina")
            .select(
                "id_turma_disciplina, id_turma, id_disciplina, taxa_aprovacao, is_concluida, "
                "disciplinas(id_disciplina, nome, descricao, semestre, area_relacionada, ra_professor)"
            )
            .eq("disciplinas.ra_professor", ra_professor)
            .execute()
        )

        dados = response.data
        dados_filtrados = [
            item for item in dados
            if item["disciplinas"] is not None and item["disciplinas"]["ra_professor"] == ra_professor
        ]

        return jsonify(dados_filtrados)
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token inválido"}), 401
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"}), 500


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

