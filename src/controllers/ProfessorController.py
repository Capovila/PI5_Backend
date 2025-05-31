import sys
import os
from flask import Blueprint, jsonify, request

from src.domain.Professor import Professor
from src.domain.exceptions.BadRequestException import BadRequestException
from src.services.ProfessorService import ProfessorService

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

class ProfessorController:
    def __init__(self):
        self.professores_bp = Blueprint("professores", __name__, url_prefix="/professores")
        self._register_routes()
        self.professorService: ProfessorService = ProfessorService()

    def _register_routes(self):
        self.professores_bp.route("/", methods=["GET"])(self.get_professores)
        self.professores_bp.route("/<int:id>", methods=["GET"])(self.get_professor_by_id)
        self.professores_bp.route("/pagination", methods=["GET"])(self.get_professor_pagination)
        self.professores_bp.route("/", methods=["POST"])(self.add_professores)
        self.professores_bp.route("/importar_csv", methods=["POST"])(self.add_professores_from_csv)
        self.professores_bp.route("/<int:id>", methods=["DELETE"])(self.delete_professor)
        self.professores_bp.route("/<int:id>", methods=["PUT"])(self.update_professor)
        self.professores_bp.route("/liberar/<int:id>", methods=["PUT"])(self.update_professor_status_to_liberado)
        self.professores_bp.route("/admin/<int:id>", methods=["PUT"])(self.update_professor_to_admin)

    def get_professores(self):
        professores = self.professorService.findProfessores()
        professores_dict = [professor.to_dict() for professor in professores]
        return jsonify(professores_dict),200

    def get_professor_by_id(self, id):
        professor = self.professorService.findProfessorById(id)
        professor_dict = professor.to_dict()
        return jsonify(professor_dict),200

    def get_professor_pagination(self):
        limit = request.args.get("limit", 10, type=int)
        page = request.args.get("page", 1, type=int)

        professores, total_professores = self.professorService.findProfessorPaginated(limit, page)
        professores_dict = [professor.to_dict() for professor in professores]

        return jsonify({
            "professores": professores_dict,
            "total_professores": total_professores,
            "actual_page": page,
            "limit_per_page": limit
        }), 200

    def add_professores(self):
        data = request.json
        ra_professor = data.get("ra_professor")
        nome = data.get("nome")
        email = data.get("email")
        senha = data.get("senha")
        is_admin = data.get("is_admin")
        is_liberado = data.get("is_liberado")

        if not ra_professor or not nome or not email or not senha or is_admin is None or is_liberado is None:
            raise BadRequestException("Campos obrigatórios não fornecidos")
        
        professor = self.professorService.addProfessor(Professor(ra_professor, nome, email, senha, is_admin, is_liberado))
        professor_dict = professor.to_dict()
        return jsonify(professor_dict), 200

    def add_professores_from_csv(self):
        payload = request.json
        csv_data = payload.get("data")

        if not csv_data:
            raise BadRequestException("Nenhum dado fornecido.")

        professores = self.professorService.addProfessoresFromCSV(csv_data)
        professores_dict = [professor.to_dict() for professor in professores]

        return jsonify({
            "message": f"{len(professores_dict)} alunos inseridos com sucesso.",
            "data": professores_dict
        }), 201

    def delete_professor(self, id):
        self.professorService.deleteProfessor(id)
        return jsonify({"message": "Professor deletado com sucesso"}), 200

    def update_professor(self, id):
        try:
            data = request.json
            ra_professor = id
            nome = data.get("nome")
            email = data.get("email")
            senha = data.get("senha")
            is_admin = data.get("is_admin")
            is_liberado = data.get("is_liberado")

            if not nome or not email or not senha or is_admin is None or is_liberado is None:
                raise BadRequestException("Campos obrigatórios não fornecidos")
            
            self.professorService.updateProfessor(Professor(ra_professor, nome, email, senha, is_admin, is_liberado))
        
            return jsonify({"message": "Professor atualizado com sucesso"}), 200
    
        except Exception as e:
                print("Erro ao atualizar professor:", e)
                return jsonify({"message": "Erro interno do servidor"}), 500

    def update_professor_status_to_liberado(self, id):
        self.professorService.liberarProfessor(id)
        return jsonify({"message": "Professor atualizado com sucesso"}), 200

    def update_professor_to_admin(self, id):
        try:
            self.professorService.updateProfessorToAdmin(id)
            return jsonify({"message": "Professor atualizado com sucesso"}), 200
        except Exception as e:
                print("Erro ao atualizar professor:", e)
                return jsonify({"message": "Erro interno do servidor"}), 500