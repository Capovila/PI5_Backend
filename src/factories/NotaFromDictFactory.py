from src.domain.Nota import Nota
from .NotaFactory import NotaFactory

class NotaFromDictFactory(NotaFactory):
    def createNota(self, data: dict) -> Nota:
        return Nota(
            ra_aluno=data["ra_aluno"],
            id_disciplina=data["id_disciplina"],
            nota=data["nota"],
            id_notas=data.get("id_notas")
        )
