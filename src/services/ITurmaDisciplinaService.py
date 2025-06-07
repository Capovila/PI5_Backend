from abc import ABC, abstractmethod
from src.domain.TurmaDisciplina import TurmaDisciplina

class ITurmaDisciplinaService(ABC):
    @abstractmethod
    def findTurmaDisciplinasByProfessor(self, email: str) -> list[dict]:
        pass

    @abstractmethod
    def addTurmaDisciplina(self, turmaDisciplina: TurmaDisciplina) -> TurmaDisciplina:
        pass

    @abstractmethod
    def updateTurmaDisciplina(self, turmaDisciplina: TurmaDisciplina):
        pass

    @abstractmethod
    def updateTurmaDisciplinaToConcluida(self, id_turma_disciplina: int):
        pass