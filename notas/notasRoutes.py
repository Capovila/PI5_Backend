import sys
import os
from flask import Blueprint, jsonify, request
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from supabase_client import supabase

notas_bp = Blueprint("notas", __name__, url_prefix="/notas")


#router.delete("/:id", notasController.deleteNotas);

#router.put("/:id", notasController.patchNotas);

@notas_bp.route("/", methods=["GET"])
def get_disciplinas():
    try:
        response = supabase.table("notas").select("*").execute()
        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"})
    
@notas_bp.route("/pagination", methods=["GET"])
def get_notas_pagination():
    try:
        data = request.json
        limit = data.get("limit", 10)  # Limite padrão de 10 registros
        page = data.get("page", 1)  # Página padrão é a 1ª

        # Calcula o intervalo de registros
        start = (page - 1) * limit
        end = start + limit - 1

        # Busca os registros no Supabase
        response = supabase.table("notas").select("*").range(start, end).execute()

        # Verifica se há registros
        if not response.data:
            return jsonify({"error": "Nenhum registro encontrado"}), 404

        return jsonify(response.data), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"}), 500
    
@notas_bp.route("/<int:id>", methods=["GET"])
def get_nota_by_id(id):
    try:
        # Busca a nota no Supabase com base no ID
        response = supabase.table("notas").select("*").eq("id_notas", id).execute()

        # Verifica se o registro foi encontrado
        if not response.data:
            return jsonify({"error": "Registro não encontrado"}), 404

        return jsonify(response.data[0]), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"}), 500

@notas_bp.route("/aluno/<int:id>", methods=["GET"])
def get_notas_by_aluno_id(id):
    try:
        # Busca as notas no Supabase com base no RA do aluno
        response = supabase.table("notas").select("*").eq("ra_aluno", id).execute()

        # Verifica se há registros
        if not response.data:
            return jsonify({"error": "Nenhum registro encontrado"}), 404

        return jsonify(response.data), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"}), 500
    
@notas_bp.route("/disciplina/<int:id>", methods=["GET"])
def get_notas_by_disciplina_id(id):
    try:
        # Busca as notas no Supabase com base no ID da disciplina
        response = supabase.table("notas").select("*").eq("id_disciplina", id).execute()

        # Verifica se há registros
        if not response.data:
            return jsonify({"error": "Nenhum registro encontrado"}), 404

        return jsonify(response.data), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"}), 500
    
@notas_bp.route("/", methods=["POST"])
def add_nota():
    try:
        data = request.json
        ra_aluno = data.get("ra_aluno")
        id_disciplina = data.get("id_disciplina")
        nota = data.get("nota")

        # Verifica se os campos obrigatórios foram fornecidos
        if not ra_aluno or not id_disciplina or nota is None:
            return jsonify({"error": "Campos obrigatórios não fornecidos"}), 400

        # Insere o registro no Supabase
        response = supabase.table("notas").insert({
            "ra_aluno": ra_aluno,
            "id_disciplina": id_disciplina,
            "nota": nota
        }).execute()

        # Verifica se a inserção foi bem-sucedida
        if not response.data:
            return jsonify({"error": "Erro ao inserir o registro"}), 400

        return jsonify({"message": "Nota inserida com sucesso"}), 201
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao inserir a nota"}), 500