from abc import ABC, abstractmethod
from src.domain.Professor import Professor

class IProfessorService(ABC):
    @abstractmethod
    def findProfessores(self) -> list[Professor]:
        pass

    @abstractmethod
    def addProfessor(self, professor: Professor) -> Professor:
        pass

    @abstractmethod
    def addProfessoresFromCSV(self, csv_data) -> list[Professor]:
        pass

    @abstractmethod
    def deleteProfessor(self, ra_professor: int):
        pass

    @abstractmethod
    def updateProfessor(self, professor: Professor):
        pass

    @abstractmethod
    def updateProfessorToAdmin(self, ra_professor: int):
        pass