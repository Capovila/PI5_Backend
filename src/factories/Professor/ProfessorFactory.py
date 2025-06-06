from abc import ABC, abstractmethod
from src.domain.Professor import Professor

class ProfessorFactory(ABC):
    @abstractmethod
    def createProfessor(self, data: dict) -> Professor:
        pass
