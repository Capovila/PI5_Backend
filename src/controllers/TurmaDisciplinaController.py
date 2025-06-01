import sys
import os
import jwt
from flask import Blueprint, jsonify, request

from src.domain.TurmaDisciplina import TurmaDisciplina
from src.domain.exceptions.BadRequestException import BadRequestException
from src.services.TurmaDisciplinaService import TurmaDisciplinaService

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

class TurmaDisciplinaController:
    def __init__(self):
        self.turma_disciplina_bp = Blueprint("turmaDisciplina", __name__, url_prefix="/turmaDisciplina")
        self._register_routes()
        self.turmaDisciplinaService: TurmaDisciplinaService = TurmaDisciplinaService()

    def _register_routes(self):
        self.turma_disciplina_bp.route("/", methods=["GET"])(self.get_turma_disciplina)
        self.turma_disciplina_bp.route("/<int:id>", methods=["GET"])(self.get_turma_disciplina_by_id)
        self.turma_disciplina_bp.route("/turma/<int:id>", methods=["GET"])(self.get_turma_disciplina_by_turma_id)
        self.turma_disciplina_bp.route("/disciplina/<int:id>", methods=["GET"])(self.get_turma_disciplina_by_disciplina_id)
        self.turma_disciplina_bp.route("/professor", methods=["GET"])(self.get_turma_disciplina_by_professor_ra)
        self.turma_disciplina_bp.route("/", methods=["POST"])(self.add_turma_disciplina)
        self.turma_disciplina_bp.route("/importar_csv", methods=["POST"])(self.add_turma_disciplina_from_csv)
        self.turma_disciplina_bp.route("/<int:id>", methods=["DELETE"])(self.delete_turma_disciplina)
        self.turma_disciplina_bp.route("/<int:id>", methods=["PUT"])(self.update_turma_disciplina)
        self.turma_disciplina_bp.route("/concluir/<int:id>", methods=["PUT"])(self.update_disciplina_status_to_concluida)

    def get_turma_disciplina(self):
        turmaDisciplinas = self.turmaDisciplinaService.findTurmaDisciplinas()
        turmaDisciplina_dict = [turmaDisciplina.to_dict() for turmaDisciplina in turmaDisciplinas]
        return jsonify(turmaDisciplina_dict),200

    def get_turma_disciplina_by_id(self, id):
        turmaDisciplina = self.turmaDisciplinaService.findTurmaDisciplinaById(id)
        turmaDisciplina_dict = turmaDisciplina.to_dict()
        return jsonify(turmaDisciplina_dict),200

    def get_turma_disciplina_by_turma_id(self, id):
        turmaDisciplinas = self.turmaDisciplinaService.findTurmaDisciplinasByTurma(id)
        turmaDisciplinas_dict = [turmaDisciplina.to_dict() for turmaDisciplina in turmaDisciplinas]
        return jsonify(turmaDisciplinas_dict), 200

    def get_turma_disciplina_by_disciplina_id(self, id):
        turmaDisciplinas = self.turmaDisciplinaService.findTurmaDisciplinasByDisciplina(id)
        turmaDisciplinas_dict = [turmaDisciplina.to_dict() for turmaDisciplina in turmaDisciplinas]
        return jsonify(turmaDisciplinas_dict), 200

    def get_turma_disciplina_by_professor_ra(self):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return jsonify({"error": "Erro ao autenticar"}), 401

        token_parts = auth_header.split()

        if len(token_parts) != 2 or token_parts[0].lower() != "bearer":
            return jsonify({"error": "Formato de token inválido"}), 401

        try:
            token = token_parts[1]
            SECRET_KEY = "tE91F+QWN88YeRb912YxdiBPIEdTWnEPBAwZOkt4PVGtdvevsMsVUT4PxzKOdTe8NmbEBfgz5NUa9CjZKCECfA=="
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"], audience="authenticated")

            email = payload["email"]

            turmaDisciplinas = self.turmaDisciplinaService.findTurmaDisciplinasByProfessor(email)
            return jsonify(turmaDisciplinas), 200
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token inválido"}), 401
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"}), 500

    def add_turma_disciplina(self):
        data = request.json
        id_turma = data.get("id_turma")
        id_disciplina = data.get("id_disciplina")
        taxa_aprovacao = data.get("taxa_aprovacao")
        is_concluida = data.get("is_concluida")

        if not id_turma or not id_disciplina or not taxa_aprovacao or is_concluida is None:
            raise BadRequestException("Campos obrigatórios não fornecidos")
        
        turmaDisciplina = self.turmaDisciplinaService.addTurmaDisciplina(TurmaDisciplina(id_turma, id_disciplina, taxa_aprovacao, is_concluida))
        turmaDisciplina_dict = turmaDisciplina.to_dict()
        return jsonify(turmaDisciplina_dict), 200

    def add_turma_disciplina_from_csv(self):
        payload = request.json
        csv_data = payload.get("data")

        if not csv_data:
            raise BadRequestException("Nenhum dado fornecido.")

        turmaDisciplinas = self.turmaDisciplinaService.addTurmaDisciplinasFromCSV(csv_data)
        turmaDisciplinas_dict = [turmaDisciplina.to_dict() for turmaDisciplina in turmaDisciplinas]

        return jsonify({
            "message": f"{len(turmaDisciplinas_dict)} turmaDisciplina inseridos com sucesso.",
            "data": turmaDisciplinas_dict
        }), 201

    def delete_turma_disciplina(self, id):
        self.turmaDisciplinaService.deleteTurmaDisciplina(id)
        return jsonify({"message": "Turma_Disciplina deletada com sucesso"}), 200

    def update_turma_disciplina(self, id):
        data = request.json
        id_turma_disciplina = id
        id_turma = data.get("id_turma")
        id_disciplina = data.get("id_disciplina")
        taxa_aprovacao = data.get("taxa_aprovacao")
        is_concluida = data.get("is_concluida")

        if not id_turma or not id_disciplina or not taxa_aprovacao or is_concluida is None:
            raise BadRequestException("Campos obrigatórios não fornecidos")
        
        self.turmaDisciplinaService.updateTurmaDisciplina(TurmaDisciplina(id_turma, id_disciplina, taxa_aprovacao, is_concluida, id_turma_disciplina))
        
        return jsonify({"message": "Turma_Disciplina atualizada com sucesso"}), 200

    def update_disciplina_status_to_concluida(self, id):
        self.turmaDisciplinaService.updateTurmaDisciplinaToConcluida(id)
        return jsonify({"message": "Turma_Disciplina atualizada com sucesso"}), 200