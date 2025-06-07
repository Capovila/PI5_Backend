import sys
import os
from flask import Blueprint, jsonify, request

from src.domain.Aluno import Aluno
from src.domain.exceptions.BadRequestException import BadRequestException
from src.services.AlunoService import AlunoService
from src.services.IAlunoService import IAlunoService

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

class AlunoController:
    def __init__(self):
        self.alunos_bp = Blueprint("alunos", __name__, url_prefix="/alunos")
        self._register_routes()
        self.alunoService:IAlunoService = AlunoService()

    def _register_routes(self):
        self.alunos_bp.route("/", methods=["GET"])(self.get_alunos)
        self.alunos_bp.route("/<int:ra_aluno>", methods=["GET"])(self.get_alunos_by_ra_aluno)
        self.alunos_bp.route("/pagination", methods=["GET"])(self.get_alunos_paginated)
        self.alunos_bp.route("/turma/<int:id_turma>", methods=["GET"])(self.get_alunos_by_turma)
        self.alunos_bp.route("/", methods=["POST"])(self.add_aluno)
        self.alunos_bp.route("/importar_csv", methods=["POST"])(self.add_alunos_from_csv)
        self.alunos_bp.route("/<int:ra_aluno>", methods=["DELETE"])(self.delete_aluno)
        self.alunos_bp.route("/<int:ra_aluno>", methods=["PUT"])(self.update_aluno)

    def get_alunos(self):
        alunos = self.alunoService.findAlunos()
        alunos_dict = [aluno.to_dict() for aluno in alunos]
        return jsonify(alunos_dict),200

    def get_alunos_by_ra_aluno(self,ra_aluno):
        aluno = self.alunoService.findAlunoByRaAluno(ra_aluno)
        aluno_dict = aluno.to_dict()
        return jsonify(aluno_dict),200

    def get_alunos_paginated(self):
        limit = request.args.get("limit", 10, type=int)
        page = request.args.get("page", 1, type=int)

        alunos, total_alunos = self.alunoService.findAlunosPaginated(limit,page)
        alunos_dict = [aluno.to_dict() for aluno in alunos]

        return jsonify({
            "alunos": alunos_dict,
            "total_alunos": total_alunos,
            "actual_page": page,
            "limit_per_page": limit
        }),200

    def get_alunos_by_turma(self, id_turma: int):
        alunos = self.alunoService.findAlunosByTurma(id_turma)
        alunos_dict = [aluno.to_dict() for aluno in alunos]
        return jsonify(alunos_dict), 200

    def add_aluno(self):
        data = request.json
        ra_aluno = data.get("ra_aluno")
        nome = data.get("nome")
        id_turma = data.get("id_turma")

        if not ra_aluno or not nome or not id_turma:
            raise BadRequestException("Campos obrigatórios não fornecidos")

        aluno = self.alunoService.addAluno(Aluno(ra_aluno, nome, id_turma))
        alunos_dict = aluno.to_dict()
        return jsonify(alunos_dict), 200

    def add_alunos_from_csv(self):
        payload = request.json
        csv_data = payload.get("data")

        if not csv_data:
            raise BadRequestException("Nenhum dado fornecido.")

        alunos = self.alunoService.addAlunoFromCSV(csv_data)
        alunos_dict = [aluno.to_dict() for aluno in alunos]

        return jsonify({
            "message": f"{len(alunos_dict)} alunos inseridos com sucesso.",
            "data": alunos_dict
        }), 201

    def delete_aluno(self, ra_aluno):
        self.alunoService.deleteAluno(ra_aluno)
        return jsonify({"message": "Aluno deletado com sucesso"}), 200

    def update_aluno(self, ra_aluno):
        data = request.json
        nome = data.get("nome")
        id_turma = data.get("id_turma")

        if not nome or not id_turma:
            raise BadRequestException("Campos obrigatórios não fornecidos")

        self.alunoService.updateAluno(ra_aluno, nome, id_turma)

        return jsonify({"message": "Aluno atualizado com sucesso"}), 200
