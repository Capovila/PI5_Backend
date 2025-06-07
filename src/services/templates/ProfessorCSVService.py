from typing import List
from src.domain.Professor import Professor
from src.factories.Professor.ProfessorFactory import ProfessorFactory
from src.repository.ProfessorRepository import ProfessorRepository
from src.services.templates.CSVImportTemplate import CSVImportTemplate


class ProfessorCSVService(CSVImportTemplate[Professor]):
    def __init__(self, factory: ProfessorFactory, repository: ProfessorRepository):
        self.factory = factory
        self.repository = repository
    
    def process_csv_line(self, linha: dict) -> Professor:
        return self.factory.createProfessor(linha)
    
    def save_entities(self, entities: List[Professor]) -> List[Professor]:
        return self.repository.saveProfessoresFromCSV(entities)