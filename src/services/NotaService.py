from src.domain.Nota import Nota
from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException
from src.repository.NotaRepository import NotaRepository


class NotaService:
    def __init__(self):
        self.notaRepository: NotaRepository = NotaRepository()

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
        notas_formatadas:list[Nota] = []
        for linha in csv_data:
            try:
                nota = Nota(
                    ra_aluno=int(linha["ra_aluno"]),
                    id_disciplina=int(linha["id_disciplina"]),
                    nota=int(linha["nota"])
                )
                notas_formatadas.append(nota)
            except (KeyError, ValueError) as e:
                print(f"Erro ao processar linha: {linha}, erro: {e}")
                continue

        if not notas_formatadas:
            raise BadRequestException("Nenhum registro válido para importar.")

        notas = self.notaRepository.saveNotasFromCSV(notas_formatadas)

        if not notas:
            raise BadRequestException("Falha ao importar o registro.")

        return notas

    def deleteNota(self, id_notas: int):
        nota = self.notaRepository.deleteNota(id_notas)
        if nota is None:
            raise ResourceNotFoundException("Nota não encontrada.")

    def updateNota(self, nota: Nota):
        nota = self.notaRepository.updateNota(nota)
        if nota is None:
            raise ResourceNotFoundException("Nota não encontrada.")
        return nota
