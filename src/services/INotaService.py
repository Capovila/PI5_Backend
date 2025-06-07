from abc import ABC, abstractmethod
from src.domain.Nota import Nota

class INotaService(ABC):
    @abstractmethod
    def findNotas(self) -> list[Nota]:
        pass

    @abstractmethod
    def findNotasPaginated(self, limit: int, page: int) -> tuple[list[Nota], int]:
        pass

    @abstractmethod
    def findNotaById(self, id_notas: int) -> Nota:
        pass

    @abstractmethod
    def findNotasByAlunoId(self, ra_aluno: int) -> list[Nota]:
        pass

    @abstractmethod
    def findNotasByAlunoIdAndDisciplinaId(self, ra_aluno: int, id_disciplina: int) -> list[Nota]:
        pass

    @abstractmethod
    def findNotasByDisciplinaId(self, id_disciplina: int) -> list[Nota]:
        pass

    @abstractmethod
    def addNota(self, nota: Nota) -> Nota:
        pass

    @abstractmethod
    def addNotasFromCSV(self, csv_data) -> list[Nota]:
        pass

    @abstractmethod
    def deleteNota(self, id_notas: int):
        pass

    @abstractmethod
    def updateNota(self, nota: Nota):
        pass