import sys
import os
from flask import Blueprint, jsonify, request

from src.domain.Nota import Nota
from src.domain.exceptions.BadRequestException import BadRequestException
from src.services.INotaService import INotaService
from src.services.NotaService import NotaService

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

class NotaController:
    def __init__(self):
        self.notas_bp = Blueprint("notas", __name__, url_prefix="/notas")
        self._register_routes()
        self.notaService: INotaService = NotaService()

    def _register_routes(self):
        self.notas_bp.route("/", methods=["GET"])(self.get_notas)
        self.notas_bp.route("/pagination", methods=["GET"])(self.get_notas_pagination)
        self.notas_bp.route("/<int:id>", methods=["GET"])(self.get_nota_by_id)
        self.notas_bp.route("/aluno/<int:id>", methods=["GET"])(self.get_notas_by_aluno_id)
        self.notas_bp.route("/disciplina/<int:id>", methods=["GET"])(self.get_notas_by_disciplina_id)
        self.notas_bp.route("/aluno/<int:idAluno>/disciplina/<int:idDisciplina>", methods=["GET"])(self.get_notas_by_aluno_id_and_disciplina_id)
        self.notas_bp.route("/", methods=["POST"])(self.add_nota)
        self.notas_bp.route("/importar_csv", methods=["POST"])(self.add_notas_from_csv)
        self.notas_bp.route("/<int:id>", methods=["DELETE"])(self.delete_nota)
        self.notas_bp.route("/<int:id>", methods=["PUT"])(self.update_nota)

    def get_notas(self):
        notas = self.notaService.findNotas()
        notas_dict = [nota.to_dict() for nota in notas]
        return jsonify(notas_dict),200

    def get_notas_pagination(self):
        limit = request.args.get("limit", 10, type=int)
        page = request.args.get("page", 1, type=int)

        notas, total_notas = self.notaService.findNotasPaginated(limit, page)
        notas_dict = [nota.to_dict() for nota in notas]

        return jsonify({
            "notas": notas_dict,
            "total_notas": total_notas,
            "actual_page": page,
            "limit_per_page": limit
        }), 200

    def get_nota_by_id(self, id):
        nota = self.notaService.findNotaById(id)
        nota_dict = nota.to_dict()
        return jsonify(nota_dict),200

    def get_notas_by_aluno_id(self, id):
        notas = self.notaService.findNotasByAlunoId(id)
        notas_dict = [nota.to_dict() for nota in notas]
        return jsonify(notas_dict), 200

    def get_notas_by_disciplina_id(self, id):
        notas = self.notaService.findNotasByDisciplinaId(id)
        notas_dict = [nota.to_dict() for nota in notas]
        return jsonify(notas_dict), 200
    
    def get_notas_by_aluno_id_and_disciplina_id(self, idAluno, idDisciplina):
        notas = self.notaService.findNotasByAlunoIdAndDisciplinaId(idAluno, idDisciplina)
        notas_dict = [nota.to_dict() for nota in notas]
        return jsonify(notas_dict), 200

    def add_nota(self):
        data = request.json
        ra_aluno = data.get("ra_aluno")
        id_disciplina = data.get("id_disciplina")
        nota = data.get("nota")

        if not ra_aluno or not id_disciplina or nota is None:
            raise BadRequestException("Campos obrigatórios não fornecidos")
        
        nota = self.notaService.addNota(Nota(ra_aluno, id_disciplina, nota))
        nota_dict = nota.to_dict()
        return jsonify(nota_dict), 200

    def add_notas_from_csv(self):
        payload = request.json
        csv_data = payload.get("data")

        if not csv_data:
            raise BadRequestException("Nenhum dado fornecido.")

        notas = self.notaService.addNotasFromCSV(csv_data)
        notas_dict = [nota.to_dict() for nota in notas]

        return jsonify({
            "message": f"{len(notas_dict)} alunos inseridos com sucesso.",
            "data": notas_dict
        }), 201

    def delete_nota(self, id):
        self.notaService.deleteNota(id)
        return jsonify({"message": "Nota deletada com sucesso"}), 200

    def update_nota(self, id):
        try:
            data = request.json
            id_notas = id
            ra_aluno = data.get("ra_aluno")
            id_disciplina = data.get("id_disciplina")
            nota = data.get("nota")

            if not ra_aluno or not id_disciplina or not nota:
                raise BadRequestException("Campos obrigatórios não fornecidos")
            
            self.notaService.updateNota(Nota(ra_aluno, id_disciplina, nota, id_notas))
            
            return jsonify({"message": "Nota atualizada com sucesso"}), 200
    
        except Exception as e:
                print("Erro ao atualizar nota:", e)
                return jsonify({"message": "Erro interno do servidor"}), 500