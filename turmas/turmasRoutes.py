import sys
import os
from flask import Blueprint, jsonify, request
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from supabase_client import supabase

turmas_bp = Blueprint("turmas", __name__, url_prefix="/turmas")

#router.get("/data", turmasController.getTurmasByDate);
#router.get("/pagination", turmasController.getTurmasPagination);
#router.get("/:id", turmasController.getTurmasById);

#router.post("/", turmasController.addTurmas);

#router.delete("/:id", turmasController.deleteTurma);

#router.put("/:id", turmasController.patchTurma);
#router.put("/graduar/:id", turmasController.graduateTurma)

@turmas_bp.route("/", methods=["GET"])
def get_turmas():
    try:
        response = supabase.table("turmas").select("*").execute()
        return jsonify(response.data)
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"})