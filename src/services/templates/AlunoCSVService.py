from typing import List
from src.domain.Aluno import Aluno
from src.factories.Aluno.AlunoFactory import AlunoFactory
from src.repository.AlunoRepository import AlunoRepository
from src.services.templates.CSVImportTemplate import CSVImportTemplate


class AlunoCSVService(CSVImportTemplate[Aluno]):
    def __init__(self, factory: AlunoFactory, repository: AlunoRepository):
        self.factory = factory
        self.repository = repository
    
    def process_csv_line(self, linha: dict) -> Aluno:
        return self.factory.createAluno(linha)
    
    def save_entities(self, entities: List[Aluno]) -> List[Aluno]:
        return self.repository.saveAlunosFromCSV(entities)