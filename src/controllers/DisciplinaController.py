import sys
import os
from flask import Blueprint, jsonify, request

from src.domain.Disciplina import Disciplina
from src.domain.exceptions.BadRequestException import BadRequestException
from src.services.DisciplinaService import DisciplinaService

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

class DisciplinaController:
    def __init__(self):
        self.disciplinas_bp = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")
        self._register_routes()
        self.disciplinaService: DisciplinaService = DisciplinaService()

    def _register_routes(self):
        self.disciplinas_bp.route("/", methods=["GET"])(self.get_disciplinas)
        self.disciplinas_bp.route("/area/<string:area_relacionada>", methods=["GET"])(self.get_disciplinas_by_area)
        self.disciplinas_bp.route("/pagination", methods=["GET"])(self.get_disciplinas_pagination)
        self.disciplinas_bp.route("/semestre/<int:semestre>", methods=["GET"])(self.get_disciplinas_by_semestre)
        self.disciplinas_bp.route("/<int:id>", methods=["GET"])(self.get_disciplina_by_id)
        self.disciplinas_bp.route("/professor/<int:ra>", methods=["GET"])(self.get_disciplinas_by_professor_ra)
        self.disciplinas_bp.route("/", methods=["POST"])(self.add_disciplina)
        self.disciplinas_bp.route("/importar_csv", methods=["POST"])(self.add_disciplinas_from_csv)
        self.disciplinas_bp.route("/<int:id>", methods=["DELETE"])(self.delete_disciplina)
        self.disciplinas_bp.route("/<int:id>", methods=["PUT"])(self.update_disciplina)

    def get_disciplinas(self):
        disciplinas = self.disciplinaService.findDisciplinas()
        disciplinas_dict = [disciplina.to_dict() for disciplina in disciplinas]
        return jsonify(disciplinas_dict),200

    def get_disciplinas_by_area(self, area_relacionada):
        """
        disciplinas = self.disciplinaService.findDisciplinasByArea(area_relacionada)
        disciplinas_dict = [disciplina.to_dict() for disciplina in disciplinas]
        return jsonify(disciplinas_dict), 200
        """

    def get_disciplinas_pagination(self):
        limit = request.args.get("limit", 10, type=int)
        page = request.args.get("page", 1, type=int)

        disciplinas, total_disciplinas = self.disciplinaService.findDisciplinasPaginated(limit, page)
        disciplinas_dict = [disciplina.to_dict() for disciplina in disciplinas]

        return jsonify({
            "disciplinas": disciplinas_dict,
            "total_disciplinas": total_disciplinas,
            "actual_page": page,
            "limit_per_page": limit
        }), 200

    def get_disciplinas_by_semestre(self, semestre):
        disciplinas = self.disciplinaService.findDisciplinasBySemestre(semestre)
        disciplinas_dict = [disciplina.to_dict() for disciplina in disciplinas]
        return jsonify(disciplinas_dict), 200

    def get_disciplina_by_id(self, id):
        disciplina = self.disciplinaService.findDisciplinaById(id)
        disciplina_dict = disciplina.to_dict()
        return jsonify(disciplina_dict),200

    def get_disciplinas_by_professor_ra(self, ra):
        disciplinas = self.disciplinaService.findDisciplinasByProfessorRa(ra)
        disciplinas_dict = [disciplina.to_dict() for disciplina in disciplinas]
        return jsonify(disciplinas_dict),200

    def add_disciplina(self):
        try:
            data = request.json
            nome = data.get("nome")
            descricao = data.get("descricao")
            semestre = data.get("semestre")
            dificuldade = data.get("dificuldade")
            ra_professor = data.get("ra_professor")

            if not nome or not descricao or not semestre or not dificuldade or not ra_professor:
                raise BadRequestException("Campos obrigatórios não fornecidos")

            disciplina = self.disciplinaService.addDisciplina(
                Disciplina(nome, descricao, semestre, ra_professor, dificuldade)
            )

            disciplina_dict = disciplina.to_dict()
            return jsonify(disciplina_dict), 200

        except Exception as e:
            print("Erro ao adicionar disciplina:", e)
            return jsonify({"message": "Erro interno do servidor"}), 500

    def add_disciplinas_from_csv(self):
        payload = request.json
        csv_data = payload.get("data")

        if not csv_data:
            raise BadRequestException("Nenhum dado fornecido.")

        disciplinas = self.disciplinaService.addDisciplinasFromCSV(csv_data)
        disciplinas_dict = [disciplina.to_dict() for disciplina in disciplinas]

        return jsonify({
            "message": f"{len(disciplinas_dict)} alunos inseridos com sucesso.",
            "data": disciplinas_dict
        }), 201

    def delete_disciplina(self, id):
        self.disciplinaService.deleteDisciplina(id)
        return jsonify({"message": "Disciplina deletada com sucesso"}), 200

    def update_disciplina(self, id):
        try:
            data = request.json
            id_disciplina = id
            nome = data.get("nome")
            descricao = data.get("descricao")
            semestre = data.get("semestre")
            dificuldade = data.get("dificuldade")
            ra_professor = data.get("ra_professor")
            teor_programacao = data.get("teor_programacao")
            teor_matematica = data.get("teor_matematica")
            teor_testes = data.get("teor_testes")
            teor_banco_dados = data.get("teor_banco_dados")
            teor_frontend = data.get("teor_frontend")
            teor_backend = data.get("teor_backend")
            teor_requisitos = data.get("teor_requisitos")
            teor_ux = data.get("teor_ux")
            teor_gestao = data.get("teor_gestao")

            if not nome or not descricao or not semestre or not ra_professor or not dificuldade:
                raise BadRequestException("Campos obrigatórios não fornecidos")
            
            self.disciplinaService.updateDisciplina(Disciplina(nome, descricao, semestre, ra_professor, dificuldade, id_disciplina))
            
            return jsonify({"message": "Disciplina atualizada com sucesso"}), 200
        
        except Exception as e:
            print("Erro ao atualizar disciplina:", e)
            return jsonify({"message": "Erro interno do servidor"}), 500