from typing import List
from src.domain.Turma import Turma
from src.repository.TurmaRepository import TurmaRepository
from src.services.templates.CSVImportTemplate import CSVImportTemplate


class TurmaCSVService(CSVImportTemplate[Turma]):
    def __init__(self, repository: TurmaRepository):
        self.repository = repository
    
    def process_csv_line(self, linha: dict) -> Turma:
        return Turma(
            data_inicio=linha["data_inicio"],
            isgraduated=bool(linha["isgraduated"]),
        )
    
    def save_entities(self, entities: List[Turma]) -> List[Turma]:
        return self.repository.saveTurmasFromCSV(entities)