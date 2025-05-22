import sys
import os
from flask import Blueprint, jsonify, request
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from supabase_client import supabase

turmas_bp = Blueprint("turmas", __name__, url_prefix="/turmas")

@turmas_bp.route("/", methods=["GET"])
def get_turmas():
    try:
        response = supabase.table("turmas").select("*").execute()
        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"})
    
@turmas_bp.route("/data", methods=["GET"])
def get_turmas_by_date():
    try:
        data_inicio = request.json.get("data_inicio")

        # Busca as turmas no Supabase com base na data de início
        response = supabase.table("turmas").select("*").eq("data_inicio", data_inicio).execute()

        # Verifica se há registros
        if not response.data:
            return jsonify({"error": "Registro não encontrado"}), 404

        return jsonify(response.data), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"}), 500
    
@turmas_bp.route("/<int:id>", methods=["GET"])
def get_professor_by_id(id):
    try:
        response = supabase.table("turmas").select("*").eq("id_turma", id).execute()
            
            # Verifica se o registro foi encontrado
        if not response.data:
            return jsonify({"error": "Registro não encontrado"}), 404
            
            # Retorna os dados do professor
        return jsonify(response.data[0])
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar registro"})
    
@turmas_bp.route("/pagination", methods=["GET"])
def get_turmas_pagination():
    try:
        data = request.json
        limit = data.get("limit", 10)  # Limite padrão de 10 registros
        page = data.get("page", 1)  # Página padrão é a 1ª

        # Calcula o intervalo de registros
        start = (page - 1) * limit
        end = start + limit - 1

        # Busca os registros no Supabase
        response = supabase.table("turmas").select("*").range(start, end).execute()

        # Verifica se há registros
        if not response.data:
            return jsonify({"error": "Nenhum registro encontrado"}), 404

        return jsonify(response.data), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"}), 500
    
@turmas_bp.route("/", methods=["POST"])
def add_turmas():
    try:
        data = request.json
        data_inicio = data.get("data_inicio")
        isgraduated = data.get("isgraduated", False)  # Valor padrão: False

        # Insere o registro no Supabase
        response = supabase.table("turmas").insert({
            "data_inicio": data_inicio,
            "isgraduated": isgraduated
        }).execute()

        # Verifica se a inserção foi bem-sucedida
        if not response.data:
            return jsonify({"error": "Erro ao inserir o registro"}), 400

        return jsonify({"message": "Turma inserida com sucesso"}), 201
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao inserir a turma"}), 500
    
@turmas_bp.route("/importar_csv", methods=["POST"])
def importar_turmas_csv():
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
    
@turmas_bp.route("/<int:id>", methods=["DELETE"])
def delete_professor(id):
    try:
        # Deleta o registro no Supabase
        response = supabase.table("turmas").delete().eq("id_turma", id).execute()

        # Verifica se o registro foi encontrado e deletado
        if not response.data:
            return jsonify({"error": "Registro não encontrado"}), 404

        return jsonify({"message": "Registro deletado com sucesso"}), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao deletar o registro"}), 500
    
    
@turmas_bp.route("/<int:id>", methods=["PUT"])
def patch_turma(id):
    try:
        data = request.json
        data_inicio = data.get("data_inicio")
        isgraduated = data.get("isgraduated")

        # Atualiza o registro no Supabase
        response = supabase.table("turmas").update({
            "data_inicio": data_inicio,
            "isgraduated": isgraduated
        }).eq("id_turma", id).execute()

        # Verifica se o registro foi encontrado e atualizado
        if not response.data:
            return jsonify({"error": "Registro não encontrado"}), 404

        return jsonify({"message": "Turma atualizada com sucesso"}), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao atualizar a turma"}), 500
    
@turmas_bp.route("/graduar/<int:id>", methods=["PUT"])
def graduate_turma(id):
    try:
        # Atualiza o campo `isgraduated` para `True`
        response = supabase.table("turmas").update({
            "isgraduated": True
        }).eq("id_turma", id).execute()

        # Verifica se o registro foi encontrado e atualizado
        if not response.data:
            return jsonify({"error": "Registro não encontrado"}), 404

        return jsonify({"message": "Turma graduada com sucesso"}), 200
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao graduar a turma"}), 500