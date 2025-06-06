from abc import ABC, abstractmethod
from src.domain.Nota import Nota

class NotaFactory(ABC):
    @abstractmethod
    def createNota(self, data: dict) -> Nota:
        pass
