from src.domain.Disciplina import Disciplina
from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException
from src.factories.Disciplina.DisciplinaFactory import DisciplinaFactory
from src.factories.Disciplina.DisciplinaFromDictFactory import DisciplinaFromDictFactory
from src.repository.DisciplinaRepository import DisciplinaRepository
from src.services.IDisciplinaService import IDisciplinaService
from src.services.templates.DisciplinaCSVService import DisciplinaCSVService

class DisciplinaService(IDisciplinaService):
    def __init__(self):
        self.disciplinaFactory: DisciplinaFactory = DisciplinaFromDictFactory()
        self.disciplinaRepository: DisciplinaRepository = DisciplinaRepository(self.disciplinaFactory)
        self.disciplinaCSVService: DisciplinaCSVService = DisciplinaCSVService(self.disciplinaFactory, self.disciplinaRepository)

    def findDisciplinas(self) -> list[Disciplina]:
        return self.disciplinaRepository.findDisciplinas()
    
    def findDisciplinasBySemestre(self, semestre: int) -> list[Disciplina]:
        disciplinas = self.disciplinaRepository.findDisciplinasBySemestre(semestre)
        if not disciplinas:
            raise ResourceNotFoundException(f"Nenhuma disciplina encontrada para o semestre {semestre}.")
        return disciplinas
    
    """
    def findDisciplinasByArea(self, area_relacionada: str) -> list[Disciplina]:
        disciplinas = self.disciplinaRepository.findDisciplinasByArea(area_relacionada)
        if not disciplinas:
            raise ResourceNotFoundException(f"Nenhuma disciplina encontrada para a área {area_relacionada}.")
        return disciplinas
    """
    
    def findDisciplinasPaginated(self, limit: int, page: int) -> tuple[list[Disciplina], int]:
        disciplinas, total_disciplinas = self.disciplinaRepository.findDisciplinasPaginated(limit,page)
        if not disciplinas and total_disciplinas == 0:
            raise ResourceNotFoundException("Nenhuma disciplina encontrada")
        if not disciplinas and total_disciplinas > 0:
            raise ResourceNotFoundException(f"Nenhuma disciplina encontrada na página {page}")
        return disciplinas, total_disciplinas
    
    def findDisciplinaById(self, id_disciplina: int) -> Disciplina:
        disciplina = self.disciplinaRepository.findDisciplinaById(id_disciplina)
        if disciplina is None:
            raise ResourceNotFoundException(f"Disciplina não encontrada.")
        return disciplina
    
    def findDisciplinasByProfessorRa(self, ra_professor: int) -> list[Disciplina]:
        disciplinas = self.disciplinaRepository.findDisciplinasByProfessorRa(ra_professor)
        if not disciplinas:
            raise ResourceNotFoundException(f"Nenhuma disciplina encontrada para o professor com RA {ra_professor}.")
        return disciplinas
    
    def addDisciplina(self, disciplina: Disciplina) -> Disciplina:
        disciplina = self.disciplinaRepository.saveDisciplina(disciplina)
        if disciplina is None:
            raise BadRequestException("Falha ao criar a disciplina.")
        return disciplina
    
    def addDisciplinasFromCSV(self, csv_data) -> list[Disciplina]:
        if isinstance(csv_data, list) and len(csv_data) > 1 and isinstance(csv_data[0], list):
            headers = csv_data[0]
            rows = csv_data[1:]
        csv_data = [dict(zip(headers, row)) for row in rows]
        return self.disciplinaCSVService.add_entities_from_csv(csv_data)
    
    def deleteDisciplina(self, id_disciplina: int):
        desciplina = self.disciplinaRepository.deleteDisciplina(id_disciplina)
        if desciplina is None:
            raise ResourceNotFoundException("Disciplina não encontrada.")
        
    def updateDisciplina(self, disciplina: Disciplina):
        disciplina = self.disciplinaRepository.updateDisciplina(disciplina)
        if disciplina is None:
            raise ResourceNotFoundException("Disciplina não encontrada.")
        return disciplina