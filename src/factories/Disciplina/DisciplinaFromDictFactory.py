from src.domain.Disciplina import Disciplina
from .DisciplinaFactory import DisciplinaFactory

class DisciplinaFromDictFactory(DisciplinaFactory):
    def createDisciplina(self, data: dict) -> Disciplina:
        return Disciplina(
            id_disciplina=data["id_disciplina"],
            nome=data["nome"],
            descricao=data["descricao"],
            semestre=data["semestre"],
            ra_professor=data["ra_professor"],
            dificuldade=data["dificuldade"],
        )
