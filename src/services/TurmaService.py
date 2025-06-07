from src.domain.Turma import Turma
from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException
from src.factories.Turma.TurmaFactory import TurmaFactory
from src.factories.Turma.TurmaFromDictFactory import TurmaFromDictFactory
from src.repository.TurmaRepository import TurmaRepository
from src.services.ITurmaService import ITurmaService
from src.services.templates.TurmaCSVService import TurmaCSVService


class TurmaService(ITurmaService):
    def __init__(self):
        self.turmaFactory: TurmaFactory = TurmaFromDictFactory()
        self.turmaRepository: TurmaRepository = TurmaRepository(self.turmaFactory)
        self.turmaCSVService: TurmaCSVService = TurmaCSVService(self.turmaRepository)

    def findTurmas(self) -> list[Turma]:
        return self.turmaRepository.findTurmas()
    
    def findTurmasByDate(self, date: str) -> list[Turma]:
        turmas = self.turmaRepository.findTurmasByDate(date)
        if not turmas:
            raise ResourceNotFoundException(f"Nenhuma turma encontrada para a data {date}.")
        return turmas
    
    def findTurmasPaginated(self, limit: int, page: int) -> tuple[list[Turma], int]:
        turmas, total_turmas = self.turmaRepository.findTurmasPaginated(limit,page)
        if not turmas and total_turmas == 0:
            raise ResourceNotFoundException("Nenhuma turma encontrada")
        if not turmas and total_turmas > 0:
            raise ResourceNotFoundException(f"Nenhuma turma encontrada na página {page}")
        return turmas, total_turmas
    
    def findTurmaById(self, id_turma: int) -> Turma:
        turma = self.turmaRepository.findTurmaById(id_turma)
        if turma is None:
            raise ResourceNotFoundException(f"Turma não encontrada.")
        return turma
    
    def addTurma(self, turma: Turma) -> Turma:
        turma = self.turmaRepository.saveTurma(turma)
        if turma is None:
            raise BadRequestException("Falha ao criar a turma.")
        return turma
    
    def addTurmasFromCSV(self, csv_data) -> list[Turma]:
        if isinstance(csv_data, list) and len(csv_data) > 1 and isinstance(csv_data[0], list):
            headers = csv_data[0]
            rows = csv_data[1:]
        csv_data = [dict(zip(headers, row)) for row in rows]
        return self.turmaCSVService.add_entities_from_csv(csv_data)
    
    def deleteTurma(self, id_turma: int):
        turma = self.turmaRepository.deleteTurma(id_turma)
        if turma is None:
            raise ResourceNotFoundException("Turma não encontrada.")
        
    def updateTurma(self, turma: Turma):
        turma = self.turmaRepository.updateTurma(turma)
        if turma is None:
            raise ResourceNotFoundException("Turma não encontrada.")
        return turma
    
    def updateTurmaToGraduate(self, id_turma: int):
        turma = self.turmaRepository.updateTurmaToGraduate(id_turma)
        if turma is None:
            raise ResourceNotFoundException("Turma não encontrada.")
        return turma