import sys
import os
from flask import Blueprint, jsonify, request

from src.domain.Turma import Turma
from src.domain.exceptions.BadRequestException import BadRequestException
from src.services.TurmaService import TurmaService

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

class TurmaController:
    def __init__(self):
        self.turmas_bp = Blueprint("turmas", __name__, url_prefix="/turmas")
        self._register_routes()
        self.turmaService: TurmaService = TurmaService()

    def _register_routes(self):
        self.turmas_bp.route("/", methods=["GET"])(self.get_turmas)
        self.turmas_bp.route("/data", methods=["GET"])(self.get_turmas_by_date)
        self.turmas_bp.route("/<int:id>", methods=["GET"])(self.get_turma_by_id)
        self.turmas_bp.route("/pagination", methods=["GET"])(self.get_turmas_pagination)
        self.turmas_bp.route("/", methods=["POST"])(self.add_turmas)
        self.turmas_bp.route("/importar_csv", methods=["POST"])(self.add_turmas_from_csv)
        self.turmas_bp.route("/<int:id>", methods=["DELETE"])(self.delete_turma)
        self.turmas_bp.route("/<int:id>", methods=["PUT"])(self.update_turma)
        self.turmas_bp.route("/graduar/<int:id>", methods=["PUT"])(self.update_turma_status_to_graduate)

    def get_turmas(self):
        turmas = self.turmaService.findTurmas()
        turmas_dict = [turma.to_dict() for turma in turmas]
        return jsonify(turmas_dict),200

    def get_turmas_by_date(self):
        data_inicio = request.args.get("data_inicio")
        turmas = self.turmaService.findTurmasByDate(data_inicio)
        turmas_dict = [turma.to_dict() for turma in turmas]
        return jsonify(turmas_dict), 200


    def get_turmas_pagination(self):
        limit = request.args.get("limit", 10, type=int)
        page = request.args.get("page", 1, type=int)

        turmas, total_turmas = self.turmaService.findTurmasPaginated(limit, page)
        turmas_dict = [turma.to_dict() for turma in turmas]

        return jsonify({
            "turmas": turmas_dict,
            "total_turmas": total_turmas,
            "actual_page": page,
            "limit_per_page": limit
        }), 200

    def get_turma_by_id(self, id): 
        turma = self.turmaService.findTurmaById(id)
        turma_dict = turma.to_dict()
        return jsonify(turma_dict),200


    def add_turmas(self):
        data = request.json
        data_inicio = data.get("data_inicio")
        isgraduated = data.get("isgraduated")

        if not data_inicio or isgraduated is None:
            raise BadRequestException("Campos obrigatórios não fornecidos")
        
        turma = self.turmaService.addTurma(Turma(data_inicio, isgraduated))
        turma_dict = turma.to_dict()
        return jsonify(turma_dict), 200


    def add_turmas_from_csv(self):
        payload = request.json
        csv_data = payload.get("data")

        if not csv_data:
            raise BadRequestException("Nenhum dado fornecido.")

        turmas = self.turmaService.addTurmasFromCSV(csv_data)
        turmas_dict = [turma.to_dict() for turma in turmas]

        return jsonify({
            "message": f"{len(turmas_dict)} alunos inseridos com sucesso.",
            "data": turmas_dict
        }), 201


    def delete_turma(self, id):
        self.turmaService.deleteTurma(id)
        return jsonify({"message": "Turma deletada com sucesso"}), 200


    def update_turma(self, id):
        try:
            data = request.json
            id_turma = id
            data_inicio = data.get("data_inicio")
            isgraduated = data.get("isgraduated")

            if not data_inicio or isgraduated is None:
                raise BadRequestException("Campos obrigatórios não fornecidos")
            
            self.turmaService.updateTurma(Turma(data_inicio, isgraduated, id_turma))
            
            return jsonify({"message": "Turma atualizada com sucesso"}), 200
        
        except Exception as e:
            print("Erro ao atualizar disciplina:", e)
            return jsonify({"message": "Erro interno do servidor"}), 500


    def update_turma_status_to_graduate(self, id):
        self.turmaService.updateTurmaToGraduate(id)
        return jsonify({"message": "Turma atualizada com sucesso"}), 200