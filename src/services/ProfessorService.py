from src.domain.Professor import Professor
from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException
from src.repository.ProfessorRepository import ProfessorRepository


class ProfessorService:
    def __init__(self):
        self.professorRepository: ProfessorRepository = ProfessorRepository()

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
        professores_formatados: list[Professor] = []
        for linha in csv_data:
            try:
                professor = Professor(
                    ra_professor= int(linha["ra_professor"]),
                    nome= linha["nome"],
                    email= linha["email"],
                    senha= linha["senha"],
                    is_admin= bool(linha["is_admin"]),
                    is_liberado= bool(linha["is_liberado"])
                )
                professores_formatados.append(professor)
            except (KeyError, ValueError) as e:
                print(f"Erro ao processar linha: {linha}, erro: {e}")
                continue

        if not professores_formatados:
            raise BadRequestException("Nenhum registro válido para importar.")

        professores = self.professorRepository.saveProfessoresFromCSV(professores_formatados)

        if not professores:
            raise BadRequestException("Falha ao importar o registro.")
        
        return professores
    
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