from abc import ABC, abstractmethod
from typing import List, Any, TypeVar, Generic

from src.domain.exceptions.BadRequestException import BadRequestException

T = TypeVar('T')

class CSVImportTemplate(ABC, Generic[T]):
    """
    Template Method for importing data from CSV.\n
    Define the algorithm, letting steps be specific for subclasses
    """
    
    def add_entities_from_csv(self, csv_data: List[dict]) -> List[T]:
        entities_formatadas = []
        
        for linha in csv_data:
            try:
                entity = self.process_csv_line(linha)
                entities_formatadas.append(entity)
            except (KeyError, ValueError) as e:
                print(f"Erro ao processar linha: {linha}, erro: {e}")
                continue
        
        if not entities_formatadas:
            raise BadRequestException("Nenhum registro válido para importar.")
        
        saved_entities = self.save_entities(entities_formatadas)
        
        if not saved_entities:
            raise BadRequestException("Falha ao importar o registro.")
        
        return saved_entities
    
    @abstractmethod
    def process_csv_line(self, linha: dict) -> T:
        pass
    
    @abstractmethod
    def save_entities(self, entities: List[T]) -> List[T]:
        pass

