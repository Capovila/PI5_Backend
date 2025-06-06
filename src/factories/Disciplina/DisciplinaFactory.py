from abc import ABC, abstractmethod
from src.domain.Disciplina import Disciplina

class DisciplinaFactory(ABC):
    @abstractmethod
    def createDisciplina(self, data: dict) -> Disciplina:
        pass
