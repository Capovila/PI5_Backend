from src.domain.Aluno import Aluno
from .AlunoFactory import AlunoFactory

class AlunoFromDictFactory(AlunoFactory):
    def createAluno(self, data: dict) -> Aluno:
        return Aluno(
            ra_aluno=data["ra_aluno"],
            nome=data["nome"],
            id_turma=data["id_turma"]
        )
