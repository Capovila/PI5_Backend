from abc import ABC, abstractmethod
from src.domain.Disciplina import Disciplina

class IDisciplinaService(ABC):
    @abstractmethod
    def findDisciplinas(self) -> list[Disciplina]:
        pass

    @abstractmethod
    def findDisciplinasBySemestre(self, semestre: int) -> list[Disciplina]:
        pass

    @abstractmethod
    def findDisciplinasPaginated(self, limit: int, page: int) -> tuple[list[Disciplina], int]:
        pass

    @abstractmethod
    def findDisciplinaById(self, id_disciplina: int) -> Disciplina:
        pass

    @abstractmethod
    def findDisciplinasByProfessorRa(self, ra_professor: int) -> list[Disciplina]:
        pass

    @abstractmethod
    def addDisciplina(self, disciplina: Disciplina) -> Disciplina:
        pass

    @abstractmethod
    def addDisciplinasFromCSV(self, csv_data) -> list[Disciplina]:
        pass

    @abstractmethod
    def deleteDisciplina(self, id_disciplina: int):
        pass

    @abstractmethod
    def updateDisciplina(self, disciplina: Disciplina):
        pass
