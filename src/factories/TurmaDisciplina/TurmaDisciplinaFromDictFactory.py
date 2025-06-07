from src.domain.TurmaDisciplina import TurmaDisciplina
from .TurmaDisciplinaFactory import TurmaDisciplinaFactory

class TurmaDisciplinaFromDictFactory(TurmaDisciplinaFactory):
    def createTurmaDisciplina(self, data: dict) -> TurmaDisciplina:
        return TurmaDisciplina(
            id_turma_disciplina=data["id_turma_disciplina"],
            id_turma=data["id_turma"],
            id_disciplina=data["id_disciplina"],
            taxa_aprovacao=data["taxa_aprovacao"],
            is_concluida=data["is_concluida"]
        )
