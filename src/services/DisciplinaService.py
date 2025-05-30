from src.domain.Disciplina import Disciplina
from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException
from src.repository.DisciplinaRepository import DisciplinaRepository


class DisciplinaService:
    def __init__(self):
        self.disciplinaRepository: DisciplinaRepository = DisciplinaRepository()

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
        disciplinas_formatadas: list[Disciplina] = []
        for linha in csv_data:
            try:
                disciplina = Disciplina(
                    nome=linha["nome"],
                    descricao=linha["descricao"],
                    semestre=int(linha["semestre"]), 
                    ra_professor=int(linha["ra_professor"]),
                    dificuldade=int(linha["dificuldade"])
                )
                disciplinas_formatadas.append(disciplina)
            except (KeyError, ValueError) as e:
                print(f"Erro ao processar linha: {linha}, erro: {e}")
                continue

        if not disciplinas_formatadas:
            raise BadRequestException("Nenhum registro válido para importar.")

        disciplinas = self.disciplinaRepository.saveDisciplinasFromCSV(disciplinas_formatadas)

        if not disciplinas:
            raise BadRequestException("Falha ao importar o registro.")
        
        return disciplinas
    
    def deleteDisciplina(self, id_disciplina: int):
        desciplina = self.disciplinaRepository.deleteDisciplina(id_disciplina)
        if desciplina is None:
            raise ResourceNotFoundException("Disciplina não encontrada.")
        
    def updateDisciplina(self, disciplina: Disciplina):
        disciplina = self.disciplinaRepository.updateDisciplina(disciplina)
        if disciplina is None:
            raise ResourceNotFoundException("Disciplina não encontrada.")
        return disciplina