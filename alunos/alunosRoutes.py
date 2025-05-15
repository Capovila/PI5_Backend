import sys
import os
from flask import Blueprint, jsonify, request
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from supabase_client import supabase

alunos_bp = Blueprint("alunos", __name__, url_prefix="/alunos")

@alunos_bp.route("/", methods=["GET"])
def get_disciplinas():
    try:
        response = supabase.table("alunos").select("*").execute()
        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"})
    
@alunos_bp.route("/<int:id>", methods=["GET"])
def get_disciplinas_by_id(id):
    try:
        response = supabase.table("alunos").select("*").eq("ra_aluno", id).execute()
        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"})
    
@alunos_bp.route("/pagination", methods=["GET"])
def get_alunos_pagination():
    try:
        data = request.json
        limit = data.get("limit", 10)  # Limite padrão de 10 registros
        page = data.get("page", 1)  # Página padrão é a 1ª

        # Calcula o intervalo de registros
        start = (page - 1) * limit
        end = start + limit - 1

        # Busca os registros no Supabase
        response = supabase.table("alunos").select("*").range(start, end).execute()

        # Verifica se há registros
        if not response.data:
            return jsonify({"error": "Nenhum registro encontrado"}), 404

        return jsonify(response.data), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"}), 500
    

@alunos_bp.route("/turma/<int:turma>", methods=["GET"])
def get_alunos_by_turma(turma):
    try:
        # Busca os alunos no Supabase com base no ID da turma
        response = supabase.table("alunos").select("*").eq("id_turma", turma).execute()

        # Verifica se há registros
        if not response.data:
            return jsonify({"error": "Nenhum registro encontrado"}), 404

        return jsonify(response.data), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"}), 500
    
@alunos_bp.route("/", methods=["POST"])
def add_aluno():
    try:
        data = request.json
        ra_aluno = data.get("ra_aluno")
        nome = data.get("nome")
        id_turma = data.get("id_turma")

        # Verifica se os campos obrigatórios foram fornecidos
        if not ra_aluno or not nome or not id_turma:
            return jsonify({"error": "Campos obrigatórios não fornecidos"}), 400

        # Insere o registro no Supabase
        response = supabase.table("alunos").insert({
            "ra_aluno": ra_aluno,
            "nome": nome,
            "id_turma": id_turma
        }).execute()

        # Verifica se a inserção foi bem-sucedida
        if not response.data:
            return jsonify({"error": "Erro ao inserir o registro"}), 400

        return jsonify({"message": "Aluno inserido com sucesso"}), 201
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao inserir o aluno"}), 500
    
@alunos_bp.route("/<int:id>", methods=["DELETE"])
def delete_aluno(id):
    try:
        # Deleta o aluno no Supabase com base no ID (RA do aluno)
        response = supabase.table("alunos").delete().eq("ra_aluno", id).execute()

        # Verifica se o registro foi encontrado e deletado
        if not response.data:
            return jsonify({"error": "Registro não encontrado"}), 404

        return jsonify({"message": "Aluno deletado com sucesso"}), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao deletar o aluno"}), 500
    

@alunos_bp.route("/<int:id>", methods=["PUT"])
def update_aluno(id):
    try:
        data = request.json
        nome = data.get("nome")
        id_turma = data.get("id_turma")

        # Verifica se os campos obrigatórios foram fornecidos
        if not nome or not id_turma:
            return jsonify({"error": "Campos obrigatórios não fornecidos"}), 400

        # Atualiza o registro no Supabase
        response = supabase.table("alunos").update({
            "nome": nome,
            "id_turma": id_turma
        }).eq("ra_aluno", id).execute()

        # Verifica se o registro foi encontrado e atualizado
        if not response.data:
            return jsonify({"error": "Registro não encontrado"}), 404

        return jsonify({"message": "Aluno atualizado com sucesso"}), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao atualizar o aluno"}), 500