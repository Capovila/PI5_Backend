import sys
import os
from flask import Blueprint, jsonify, request
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from supabase_client import supabase

notas_bp = Blueprint("notas", __name__, url_prefix="/notas")


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
    
@notas_bp.route("/importar_csv", methods=["POST"])
def importar_notas_csv():
    try:
        payload = request.json
        csv_data = payload.get("data")
        print("CSV Data:", csv_data)

        if not csv_data:
            return jsonify({"error": "Nenhum dado fornecido."}), 400

        notas_formatadas = []
        for linha in csv_data:
            try:
                nota = {
                    "ra_aluno": int(linha["ra_aluno"]),
                    "id_disciplina": int(linha["id_disciplina"]),
                    "nota": float(linha["nota"])
                }
                notas_formatadas.append(nota)
            except (KeyError, ValueError) as e:
                print(f"Erro ao processar linha: {linha}, erro: {e}")
                continue

        if not notas_formatadas:
            return jsonify({"error": "Nenhum registro válido para importar."}), 400

        response = supabase.table("notas").insert(notas_formatadas).execute()

        return jsonify({
            "message": f"{len(notas_formatadas)} notas inseridos com sucesso.",
            "data": response.data
        }), 201

    except Exception as err:
        print("Erro ao importar notas via CSV:", err)
        return {"error": str(err)}, 500
    
@notas_bp.route("/<int:id>", methods=["DELETE"])
def delete_nota(id):
    try:
        # Deleta a nota no Supabase com base no ID
        response = supabase.table("notas").delete().eq("id_notas", id).execute()

        # Verifica se algum registro foi deletado
        if not response.data:
            return jsonify({"error": "Registro não encontrado"}), 404

        return jsonify({"message": "Nota deletada com sucesso"}), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao deletar a nota"}), 500
    
@notas_bp.route("/<int:id>", methods=["PUT"])
def update_nota(id):
    try:
        data = request.json
        ra_aluno = data.get("ra_aluno")
        id_disciplina = data.get("id_disciplina")
        nota = data.get("nota")

        # Verifica se pelo menos um campo foi fornecido para atualização
        if ra_aluno is None and id_disciplina is None and nota is None:
            return jsonify({"error": "Nenhum campo para atualizar"}), 400

        update_fields = {}
        if ra_aluno is not None:
            update_fields["ra_aluno"] = ra_aluno
        if id_disciplina is not None:
            update_fields["id_disciplina"] = id_disciplina
        if nota is not None:
            update_fields["nota"] = nota

        response = supabase.table("notas").update(update_fields).eq("id_notas", id).execute()

        if not response.data:
            return jsonify({"error": "Registro não encontrado"}), 404

        return jsonify({"message": "Nota atualizada com sucesso"}), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao atualizar a nota"}), 500