from src.domain.TurmaDisciplina import TurmaDisciplina
from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException
from src.repository.TurmaDisciplinaRepository import TurmaDisciplinaRepository


class TurmaDisciplinaService:
    def __init__(self):
        self.turmaDisciplinaRepository: TurmaDisciplinaRepository = TurmaDisciplinaRepository()

    def findTurmaDisciplinas(self) -> list[TurmaDisciplina]:
        return self.turmaDisciplinaRepository.findTurmaDisciplinas()
    
    def findTurmaDisciplinaById(self, id_turma_disciplina: int) -> TurmaDisciplina:
        turmaDisciplina = self.turmaDisciplinaRepository.findTurmaDisciplinaById(id_turma_disciplina)
        if turmaDisciplina is None:
            raise ResourceNotFoundException(f"Turma_Disciplina não encontrada.")
        return turmaDisciplina
    
    def findTurmaDisciplinasByTurma(self, id_turma: int) -> list[TurmaDisciplina]:
        turmaDisciplina = self.turmaDisciplinaRepository.findTurmaDisciplinasByTurma(id_turma)
        if not turmaDisciplina:
            raise ResourceNotFoundException(f"Nenhuma disciplina encontrada.")
        return turmaDisciplina
    
    def findTurmaDisciplinasByDisciplina(self, id_disciplina: int) -> list[TurmaDisciplina]:
        turmaDisciplina = self.turmaDisciplinaRepository.findTurmaDisciplinasByDisciplina(id_disciplina)
        if not turmaDisciplina:
            raise ResourceNotFoundException(f"Nenhuma disciplina encontrada.")
        return turmaDisciplina
    
    def findTurmaDisciplinasByProfessor(self, email: str) -> list[dict]:
        turmaDisciplinas = self.turmaDisciplinaRepository.findTurmaDisciplinasByProfessor(email)
        if not turmaDisciplinas:
            raise ResourceNotFoundException(f"Nenhuma disciplina encontrada.")
        return turmaDisciplinas
    
    def addTurmaDisciplina(self, turmaDisciplina: TurmaDisciplina) -> TurmaDisciplina:
        turmaDisciplina = self.turmaDisciplinaRepository.saveTurmaDisciplina(turmaDisciplina)
        if turmaDisciplina is None:
            raise BadRequestException("Falha ao criar a Turma_Disciplina.")
        return turmaDisciplina
    
    def addTurmaDisciplinasFromCSV(self, csv_data) -> list[TurmaDisciplina]:
        turmaDisciplinas_formatadas: list[TurmaDisciplina] = []
        for linha in csv_data:
            try:
                turmaDisciplina = TurmaDisciplina(
                    id_turma= int(linha["id_turma"]),
                    id_disciplina= int(linha["id_disciplina"]),
                    taxa_aprovacao= float(linha["taxa_aprovacao"]),
                    is_concluida= bool(linha["is_concluida"])
                )
                turmaDisciplinas_formatadas.append(turmaDisciplina)
            except (KeyError, ValueError) as e:
                print(f"Erro ao processar linha: {linha}, erro: {e}")
                continue

        if not turmaDisciplinas_formatadas:
            raise BadRequestException("Nenhum registro válido para importar.")

        turmaDisciplina = self.turmaDisciplinaRepository.saveTurmaDisciplinasFromCSV(turmaDisciplinas_formatadas)

        if not turmaDisciplina:
            raise BadRequestException("Falha ao importar o registro.")
        
        return turmaDisciplina
    
    def deleteTurmaDisciplina(self, id_turma_disciplina: int):
        turmaDisciplina = self.turmaDisciplinaRepository.deleteTurmaDisciplina(id_turma_disciplina)
        if turmaDisciplina is None:
            raise ResourceNotFoundException("Turma_Disciplina não encontrada.")
        
    def updateTurmaDisciplina(self, turmaDisciplina: TurmaDisciplina):
        turmaDisciplina = self.turmaDisciplinaRepository.updateTurmaDisciplina(turmaDisciplina)
        if turmaDisciplina is None:
            raise ResourceNotFoundException("Turma_Disciplina não encontrada.")
        return turmaDisciplina
        
    def updateTurmaDisciplinaToConcluida(self, id_turma_disciplina: int):
        turmaDisciplina = self.turmaDisciplinaRepository.updateTurmaDisciplinaToConcluida(id_turma_disciplina)
        if turmaDisciplina is None:
            raise ResourceNotFoundException("Turma_Disciplina não encontrada.")
        return turmaDisciplina