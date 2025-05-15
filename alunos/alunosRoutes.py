import sys
import os
from flask import Blueprint, jsonify, request
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from supabase_client import supabase

alunos_bp = Blueprint("alunos", __name__, url_prefix="/alunos")

#router.get("/", alunosController.getAlunos);
#router.get("/pagination", alunosController.getAlunosPagination);
#router.get("/:id", alunosController.getAlunosById);
#router.get("/turma/:turma", alunosController.getAlunosByTurma);

#router.post("/", alunosController.addAluno);

#router.delete("/:id", alunosController.deleteAluno);

#router.put("/:id", alunosController.patchAluno);