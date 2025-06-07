from abc import ABC, abstractmethod
from src.domain.Turma import Turma

class TurmaFactory(ABC):
    @abstractmethod
    def createTurma(self, data: dict) -> Turma:
        pass
