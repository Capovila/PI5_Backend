from src.domain.Turma import Turma
from .TurmaFactory import TurmaFactory

class TurmaFromDictFactory(TurmaFactory):
    def createTurma(self, data: dict) -> Turma:
        return Turma(
            id_turma=data["id_turma"],
            data_inicio=data["data_inicio"],
            isgraduated=data["isgraduated"],
        )
