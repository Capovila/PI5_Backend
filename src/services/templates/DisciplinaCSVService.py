from typing import List
from src.domain.Disciplina import Disciplina
from src.factories.Disciplina.DisciplinaFactory import DisciplinaFactory
from src.repository.DisciplinaRepository import DisciplinaRepository
from src.services.templates.CSVImportTemplate import CSVImportTemplate


class DisciplinaCSVService(CSVImportTemplate[Disciplina]):
    def __init__(self, factory: DisciplinaFactory, repository: DisciplinaRepository):
        self.factory = factory
        self.repository = repository
    
    def process_csv_line(self, linha: dict) -> Disciplina:
        return self.factory.createDisciplina(linha)
    
    def save_entities(self, entities: List[Disciplina]) -> List[Disciplina]:
        return self.repository.saveDisciplinasFromCSV(entities)