from src.factories.AlunoFactory import AlunoFactory
from src.factories.AlunoFromDictFactory import AlunoFromDictFactory
from src.domain.Aluno import Aluno
from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException
from src.repository.AlunoRepository import AlunoRepository

class AlunoService:
    def __init__(self):
        self.alunoFactory: AlunoFactory = AlunoFromDictFactory()
        self.alunoRepository: AlunoRepository = AlunoRepository(self.alunoFactory)

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

    def addAlunoFromCSV(self, csv_data) -> list[Aluno]:
        alunos_formatados:list[Aluno] = []
        for linha in csv_data:
            try:
                aluno = self.alunoFactory.createAluno(linha)
                alunos_formatados.append(aluno)
            except (KeyError, ValueError) as e:
                print(f"Erro ao processar linha: {linha}, erro: {e}")
                continue

        if not alunos_formatados:
            raise BadRequestException("Nenhum registro válido para importar.")

        alunos = self.alunoRepository.saveAlunosFromCSV(alunos_formatados)

        if not alunos:
            raise BadRequestException("Falha ao importar o registro.")

        return alunos

    def deleteAluno(self, ra_aluno: int):
        aluno = self.alunoRepository.deleteAluno(ra_aluno)
        if aluno is None:
            raise ResourceNotFoundException("Aluno não encontrado.")

    def updateAluno(self, ra_aluno: int, nome: str, id_turma: int):
        aluno = self.alunoRepository.updateAluno(ra_aluno, nome, id_turma)
        if aluno is None:
            raise ResourceNotFoundException("Aluno não encontrado.")
