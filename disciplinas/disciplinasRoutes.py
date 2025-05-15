import sys
import os
from flask import Blueprint, jsonify, request
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from supabase_client import supabase

disciplinas_bp = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")


@disciplinas_bp.route("/", methods=["GET"])
def get_disciplinas():
    try:
        response = supabase.table("disciplinas").select("*").execute()
        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"})
    
@disciplinas_bp.route("/area/<string:area_relacionada>", methods=["GET"])
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
    
@disciplinas_bp.route("/pagination", methods=["GET"])
def get_disciplinas_pagination():
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
    
@disciplinas_bp.route("/semestre/<int:semestre>", methods=["GET"])
def get_disciplinas_by_semestre(semestre):
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
    
@disciplinas_bp.route("/<int:id>", methods=["GET"])
def get_disciplina_by_id(id):
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
    
@disciplinas_bp.route("/professor/<int:ra>", methods=["GET"])
def get_disciplinas_by_professor_ra(ra):
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
    

@disciplinas_bp.route("/", methods=["POST"])
def add_disciplina():
    try:
        data = request.json
        nome = data.get("nome")
        descricao = data.get("descricao")
        area_relacionada = data.get("area_relacionada")
        semestre = data.get("semestre")
        ra_professor = data.get("ra_professor")

        # Verifica se os campos obrigatórios foram fornecidos
        if not nome or not area_relacionada or not semestre or not ra_professor:
            return jsonify({"error": "Campos obrigatórios não fornecidos"}), 400

        # Insere o registro no Supabase
        response = supabase.table("disciplinas").insert({
            "nome": nome,
            "descricao": descricao,
            "area_relacionada": area_relacionada,
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
    
@disciplinas_bp.route("/<int:id>", methods=["DELETE"])
def delete_disciplina(id):
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
    

@disciplinas_bp.route("/<int:id>", methods=["PUT"])
def update_disciplina(id):
    try:
        data = request.json
        nome = data.get("nome")
        descricao = data.get("descricao")
        area_relacionada = data.get("area_relacionada")
        semestre = data.get("semestre")
        ra_professor = data.get("ra_professor")

        # Verifica se os campos obrigatórios foram fornecidos
        if not nome or not area_relacionada or not semestre or not ra_professor:
            return jsonify({"error": "Campos obrigatórios não fornecidos"}), 400

        # Atualiza o registro no Supabase
        response = supabase.table("disciplinas").update({
            "nome": nome,
            "descricao": descricao,
            "area_relacionada": area_relacionada,
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