import sys
import os
from flask import Blueprint, jsonify
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from supabase_client import supabase

professores_bp = Blueprint("professores", __name__, url_prefix="/professores")

# router.get("/pagination", professoresController.getProfessoresPagination);

# router.post("/", professoresController.addProfessores);

# router.delete("/:id", professoresController.deleteProfessor);

# router.put("/:id", professoresController.patchProfessor);
# router.put("/liberar/:id", professoresController.liberarProfessor);
# router.put("/admin/:id", professoresController.professorAdmin);

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
    


