from abc import ABC, abstractmethod
from src.domain.Aluno import Aluno

class IAlunoService(ABC):
    @abstractmethod
    def findAlunos(self) -> list[Aluno]:
        pass

    @abstractmethod
    def findAlunosPaginated(self, limit: int, page: int) -> tuple[list[Aluno], int]:
        pass

    @abstractmethod
    def findAlunosByTurma(self, id_turma: int) -> list[Aluno]:
        pass

    @abstractmethod
    def addAluno(self, aluno: Aluno) -> Aluno:
        pass

    @abstractmethod
    def addAlunosFromCSV(self, csv_data) -> list[Aluno]:
        pass

    @abstractmethod
    def deleteAluno(self, ra_aluno: int):
        pass

    @abstractmethod
    def updateAluno(self, aluno: Aluno):
        pass