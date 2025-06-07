import csv
from src.domain.TurmaDisciplina import TurmaDisciplina
from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException
from src.factories.TurmaDisciplina.TurmaDisciplinaFromDictFactory import TurmaDisciplinaFromDictFactory
from src.factories.TurmaDisciplina.TurmaDisciplinaFactory import TurmaDisciplinaFactory
from src.repository.TurmaDisciplinaRepository import TurmaDisciplinaRepository
from src.services.templates.TurmaDisciplinaCSVService import TurmaDisciplinaCSVService


class TurmaDisciplinaService:
    def __init__(self):
        self.turmaDisciplinaFactory: TurmaDisciplinaFactory = TurmaDisciplinaFromDictFactory()
        self.turmaDisciplinaRepository: TurmaDisciplinaRepository = TurmaDisciplinaRepository(self.turmaDisciplinaFactory)
        self.turmaDisciplinaCSVService: TurmaDisciplinaCSVService = TurmaDisciplinaCSVService(self.turmaDisciplinaRepository)

    def findTurmaDisciplinas(self) -> list[TurmaDisciplina]:
        return self.turmaDisciplinaRepository.findTurmaDisciplinas()
    
    def findTurmaDisciplinaById(self, id_turma_disciplina: int) -> TurmaDisciplina:
        turmaDisciplina = self.turmaDisciplinaRepository.findTurmaDisciplinaById(id_turma_disciplina)
        if turmaDisciplina is None:
            raise ResourceNotFoundException(f"Turma_Disciplina não encontrada.")
        return turmaDisciplina
    
    def findTurmaDisciplinasByTurma(self, id_turma: int) -> list[TurmaDisciplina]:
        turmaDisciplina = self.turmaDisciplinaRepository.findTurmaDisciplinasByTurma(id_turma)
        if not turmaDisciplina:
            raise ResourceNotFoundException(f"Nenhuma disciplina encontrada.")
        return turmaDisciplina
    
    def findTurmaDisciplinasByDisciplina(self, id_disciplina: int) -> list[TurmaDisciplina]:
        turmaDisciplina = self.turmaDisciplinaRepository.findTurmaDisciplinasByDisciplina(id_disciplina)
        if not turmaDisciplina:
            raise ResourceNotFoundException(f"Nenhuma disciplina encontrada.")
        return turmaDisciplina
    
    def findTurmaDisciplinasByProfessor(self, email: str) -> list[dict]:
        turmaDisciplinas = self.turmaDisciplinaRepository.findTurmaDisciplinasByProfessor(email)
        if not turmaDisciplinas:
            raise ResourceNotFoundException(f"Nenhuma disciplina encontrada.")
        return turmaDisciplinas
    
    def addTurmaDisciplina(self, turmaDisciplina: TurmaDisciplina) -> TurmaDisciplina:
        turmaDisciplina = self.turmaDisciplinaRepository.saveTurmaDisciplina(turmaDisciplina)
        if turmaDisciplina is None:
            raise BadRequestException("Falha ao criar a Turma_Disciplina.")
        return turmaDisciplina
    
    def addTurmaDisciplinasFromCSV(self, csv_data) -> list[TurmaDisciplina]:
        if isinstance(csv_data, list) and len(csv_data) > 1 and isinstance(csv_data[0], list):
            headers = csv_data[0]
            rows = csv_data[1:]
        csv_data = [dict(zip(headers, row)) for row in rows]
        return self.turmaDisciplinaCSVService.add_entities_from_csv(csv_data)

    def deleteTurmaDisciplina(self, id_turma_disciplina: int):
        turmaDisciplina = self.turmaDisciplinaRepository.deleteTurmaDisciplina(id_turma_disciplina)
        if turmaDisciplina is None:
            raise ResourceNotFoundException("Turma_Disciplina não encontrada.")
        
    def updateTurmaDisciplina(self, turmaDisciplina: TurmaDisciplina):
        turmaDisciplina = self.turmaDisciplinaRepository.updateTurmaDisciplina(turmaDisciplina)
        if turmaDisciplina is None:
            raise ResourceNotFoundException("Turma_Disciplina não encontrada.")
        return turmaDisciplina
        
    def updateTurmaDisciplinaToConcluida(self, id_turma_disciplina: int):
        turmaDisciplina = self.turmaDisciplinaRepository.updateTurmaDisciplinaToConcluida(id_turma_disciplina)
        if turmaDisciplina is None:
            raise ResourceNotFoundException("Turma_Disciplina não encontrada.")
        return turmaDisciplina