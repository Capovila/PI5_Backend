from src.domain.Turma import Turma
from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException
from src.repository.TurmaRepository import TurmaRepository


class TurmaService:
    def __init__(self):
        self.turmaRepository: TurmaRepository = TurmaRepository()

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
        turmas_formatadas: list[Turma] = []
        for linha in csv_data:
            try:
                turma = Turma(
                    data_inicio= linha["data_inicio"],
                    isgraduated= bool(linha["isgraduated"]),
                )
                turmas_formatadas.append(turma)
            except (KeyError, ValueError) as e:
                print(f"Erro ao processar linha: {linha}, erro: {e}")
                continue

        if not turmas_formatadas:
            raise BadRequestException("Nenhum registro válido para importar.")

        turmas = self.turmaRepository.saveTurmasFromCSV(turmas_formatadas)

        if not turmas:
            raise BadRequestException("Falha ao importar o registro.")
        
        return turmas
    
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