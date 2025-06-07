from src.domain.Professor import Professor
from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException
from src.factories.Professor.ProfessorFactory import ProfessorFactory
from src.factories.Professor.ProfessorFromDictFactory import ProfessorFromDictFactory
from src.repository.ProfessorRepository import ProfessorRepository
from src.services.IProfessorService import IProfessorService
from src.services.templates.ProfessorCSVService import ProfessorCSVService

class ProfessorService(IProfessorService):
    def __init__(self):
        self.professorFactory: ProfessorFactory = ProfessorFromDictFactory()
        self.professorRepository: ProfessorRepository = ProfessorRepository(self.professorFactory)
        self.professorCSVService: ProfessorCSVService = ProfessorCSVService(self.professorFactory, self.professorRepository)

    def findProfessores(self) -> list[Professor]:
        return self.professorRepository.findProfessores()
    
    def findProfessorById(self, ra_professor: int) -> Professor:
        professor = self.professorRepository.findProfessorById(ra_professor)
        if professor is None:
            raise ResourceNotFoundException(f"Professor não encontrado.")
        return professor
    
    def findProfessorPaginated(self, limit: int, page: int) -> tuple[list[Professor], int]:
        professores, total_professores = self.professorRepository.findProfessoresPaginated(limit,page)
        if not professores and total_professores == 0:
            raise ResourceNotFoundException("Nenhum professor encontrado")
        if not professores and total_professores > 0:
            raise ResourceNotFoundException(f"Nenhum professor encontrado na página {page}")
        return professores, total_professores
    
    def addProfessor(self, professor: Professor) -> Professor:
        professor = self.professorRepository.saveProfessor(professor)
        if professor is None:
            raise BadRequestException("Falha ao criar o professor.")
        return professor
    
    def addProfessoresFromCSV(self, csv_data) -> list[Professor]:
        if isinstance(csv_data, list) and len(csv_data) > 1 and isinstance(csv_data[0], list):
            headers = csv_data[0]
            rows = csv_data[1:]
        csv_data = [dict(zip(headers, row)) for row in rows]
        return self.professorCSVService.add_entities_from_csv(csv_data)
    
    def deleteProfessor(self, ra_professor: int):
        professor = self.professorRepository.deleteProfessor(ra_professor)
        if professor is None:
            raise ResourceNotFoundException("Professor não encontrado.")
        
    def updateProfessor(self, professor: Professor):
        professor = self.professorRepository.updateProfessor(professor)
        if professor is None:
            raise ResourceNotFoundException("Professor não encontrado.")
        return professor
    
    def updateProfessorToAdmin(self, ra_professor: int):
        professor = self.professorRepository.updateProfessorToAdmin(ra_professor)
        if professor is None:
            raise ResourceNotFoundException("Professor não encontrado.")
        return professor
    
    def liberarProfessor(self, ra_professor: int):
        professor = self.professorRepository.liberarProfessor(ra_professor)
        if professor is None:
            raise ResourceNotFoundException("Professor não encontrado.")
        return professor