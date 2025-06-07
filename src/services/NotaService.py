from src.factories.Nota.NotaFromDictFactory import NotaFromDictFactory
from src.factories.Nota.NotaFactory import NotaFactory
from src.domain.Nota import Nota
from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException
from src.repository.NotaRepository import NotaRepository
from src.services.INotaService import INotaService
from src.services.templates.NotaCSVService import NotaCSVService

class NotaService(INotaService):
    def __init__(self):
        self.notaFactory: NotaFactory = NotaFromDictFactory()
        self.notaRepository: NotaRepository = NotaRepository(self.notaFactory)
        self.notaCSVService: NotaCSVService = NotaCSVService(self.notaFactory, self.notaRepository)

    def findNotas(self) -> list[Nota]:
        return self.notaRepository.findNotas()

    def findNotasPaginated(self, limit:int, page:int) -> tuple[list[Nota], int]:
        notas, total_notas = self.notaRepository.findNotasPaginated(limit,page)
        if not notas and total_notas == 0:
            raise ResourceNotFoundException("Nenhuma nota encontrada")
        if not notas and total_notas > 0:
            raise ResourceNotFoundException(f"Nenhuma nota encontrada na página {page}")
        return notas, total_notas

    def findNotaById(self, id_notas:int) -> Nota:
        nota = self.notaRepository.findNotaById(id_notas)
        if nota is None:
            raise ResourceNotFoundException(f"Nota não encontrada.")
        return nota

    def findNotasByAlunoId(self, ra_aluno: int) -> list[Nota]:
        notas = self.notaRepository.findNotasByAlunoId(ra_aluno)
        if not notas:
            raise ResourceNotFoundException(f"Notas não encontradas.")
        return notas
    
    def findNotasByAlunoIdAndDisciplinaId(self, ra_aluno: int, id_disciplina: int) -> list[Nota]:
        notas = self.notaRepository.findNotasByAlunoIdAndDisciplinaId(ra_aluno, id_disciplina)
        if not notas:
            raise ResourceNotFoundException(f"Notas não encontradas para o aluno {ra_aluno} na disciplina {id_disciplina}.")
        return notas
    
    def findNotasByDisciplinaId(self, id_disciplina: int) -> list[Nota]:
        notas = self.notaRepository.findNotasByDisciplinaId(id_disciplina)
        if not notas:
            raise ResourceNotFoundException(f"Notas não encontradas.")
        return notas

    def addNota(self, nota: Nota) -> Nota:
        nota = self.notaRepository.saveNota(nota)
        if nota is None:
            raise BadRequestException("Falha ao criar a nota")
        return nota

    def addNotasFromCSV(self, csv_data) -> list[Nota]:
        if isinstance(csv_data, list) and len(csv_data) > 1 and isinstance(csv_data[0], list):
            headers = csv_data[0]
            rows = csv_data[1:]
        csv_data = [dict(zip(headers, row)) for row in rows]
        return self.notaCSVService.add_entities_from_csv(csv_data)

    def deleteNota(self, id_notas: int):
        nota = self.notaRepository.deleteNota(id_notas)
        if nota is None:
            raise ResourceNotFoundException("Nota não encontrada.")

    def updateNota(self, nota: Nota):
        nota = self.notaRepository.updateNota(nota)
        if nota is None:
            raise ResourceNotFoundException("Nota não encontrada.")
        return nota
