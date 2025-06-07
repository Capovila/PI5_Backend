from typing import List
from src.domain.Nota import Nota
from src.factories.Nota.NotaFactory import NotaFactory
from src.repository.NotaRepository import NotaRepository
from src.services.templates.CSVImportTemplate import CSVImportTemplate


class NotaCSVService(CSVImportTemplate[Nota]):
    def __init__(self, factory: NotaFactory, repository: NotaRepository):
        self.factory = factory
        self.repository = repository
    
    def process_csv_line(self, linha: dict) -> Nota:
        linha['id_notas'] = int(linha['id_notas'])
        linha['ra_aluno'] = int(linha['ra_aluno'])
        linha['id_disciplina'] = int(linha['id_disciplina'])
        linha['nota'] = float(linha['nota'])
        
        return self.factory.createNota(linha)
    
    def save_entities(self, entities: List[Nota]) -> List[Nota]:
        return self.repository.saveNotasFromCSV(entities)