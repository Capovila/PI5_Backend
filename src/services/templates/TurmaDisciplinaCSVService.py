from typing import List
from src.domain.TurmaDisciplina import TurmaDisciplina
from src.repository.TurmaDisciplinaRepository import TurmaDisciplinaRepository
from src.services.templates.CSVImportTemplate import CSVImportTemplate

class TurmaDisciplinaCSVService(CSVImportTemplate[TurmaDisciplina]):
    def __init__(self, repository: TurmaDisciplinaRepository):
        self.repository = repository
    
    def process_csv_line(self, linha: dict) -> TurmaDisciplina:
        is_concluida_str = linha.get("is_concluida", "false").strip().lower()
        is_concluida_val = is_concluida_str == 'true'
        print(f"Processando linha: {linha}, is_concluida: {is_concluida_val}")
        
        return TurmaDisciplina(
            id_turma=int(linha["id_turma"]),
            id_disciplina=int(linha["id_disciplina"]),
            taxa_aprovacao=int(linha["taxa_aprovacao"]),
            is_concluida=is_concluida_val
        )
    
    def save_entities(self, entities: List[TurmaDisciplina]) -> List[TurmaDisciplina]:
        return self.repository.saveTurmaDisciplinasFromCSV(entities)