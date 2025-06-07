from abc import ABC, abstractmethod
from src.domain.TurmaDisciplina import TurmaDisciplina

class TurmaDisciplinaFactory(ABC):
    @abstractmethod
    def createTurmaDisciplina(self, data: dict) -> TurmaDisciplina:
        pass
