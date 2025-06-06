from abc import ABC, abstractmethod
from src.domain.Aluno import Aluno

class AlunoFactory(ABC):
    @abstractmethod
    def createAluno(self, data: dict) -> Aluno:
        pass
