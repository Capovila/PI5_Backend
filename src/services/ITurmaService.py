from abc import ABC, abstractmethod
from src.domain.Turma import Turma

class ITurmaService(ABC):
    @abstractmethod
    def findTurmas(self) -> list[Turma]:
        pass

    @abstractmethod
    def findTurmasByDate(self, date: str) -> list[Turma]:
        pass

    @abstractmethod
    def addTurma(self, turma: Turma) -> Turma:
        pass

    @abstractmethod
    def addTurmasFromCSV(self, csv_data) -> list[Turma]:
        pass

    @abstractmethod
    def deleteTurma(self, id_turma: int):
        pass

    @abstractmethod
    def updateTurma(self, turma: Turma):
        pass