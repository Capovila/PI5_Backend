from src.factories.Aluno.AlunoFactory import AlunoFactory
from src.factories.Aluno.AlunoFromDictFactory import AlunoFromDictFactory
from src.domain.Aluno import Aluno
from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException
from src.repository.AlunoRepository import AlunoRepository
from src.services.IAlunoService import IAlunoService
from src.services.templates.AlunoCSVService import AlunoCSVService

class AlunoService(IAlunoService):
    def __init__(self):
        self.alunoFactory: AlunoFactory = AlunoFromDictFactory()
        self.alunoRepository: AlunoRepository = AlunoRepository(self.alunoFactory)
        self.alunoCSVService: AlunoCSVService = AlunoCSVService(self.alunoFactory, self.alunoRepository)

    def findAlunos(self) -> list[Aluno]:
        return self.alunoRepository.findAlunos()

    def findAlunoByRaAluno(self, aluno_id:int) -> Aluno:
        aluno = self.alunoRepository.findAlunoByRaAluno(aluno_id)
        if aluno is None:
            raise ResourceNotFoundException(f"Aluno não encontrado.")
        return aluno

    def findAlunosPaginated(self, limit:int, page:int) -> tuple[list[Aluno], int]:
        alunos, total_alunos = self.alunoRepository.findAlunosPaginated(limit,page)
        if not alunos and total_alunos == 0:
            raise ResourceNotFoundException("Nenhum aluno encontrado")
        if not alunos and total_alunos > 0:
            raise ResourceNotFoundException(f"Nenhum aluno encontrado na página {page}")
        return alunos, total_alunos

    def findAlunosByTurma(self, id_turma: int) -> list[Aluno]:
        alunos = self.alunoRepository.findAlunosByTurma(id_turma)
        if not alunos:
            raise ResourceNotFoundException(f"Alunos não encontrados.")
        return alunos

    def addAluno(self, aluno: Aluno) -> Aluno:
        aluno = self.alunoRepository.saveAluno(aluno)
        if aluno is None:
            raise BadRequestException("Falha ao criar o usuário")
        return aluno

    def addAlunosFromCSV(self, csv_data) -> list[Aluno]:
        if isinstance(csv_data, list) and len(csv_data) > 1 and isinstance(csv_data[0], list):
            headers = csv_data[0]
            rows = csv_data[1:]
        csv_data = [dict(zip(headers, row)) for row in rows]
        return self.alunoCSVService.add_entities_from_csv(csv_data)

    def deleteAluno(self, ra_aluno: int):
        aluno = self.alunoRepository.deleteAluno(ra_aluno)
        if aluno is None:
            raise ResourceNotFoundException("Aluno não encontrado.")

    def updateAluno(self, ra_aluno: int, nome: str, id_turma: int):
        aluno = self.alunoRepository.updateAluno(ra_aluno, nome, id_turma)
        if aluno is None:
            raise ResourceNotFoundException("Aluno não encontrado.")
