from src.domain.Turma import Turma
from src.factories.Turma.TurmaFactory import TurmaFactory
from src.infrastructure.supabase_client import supabase

class TurmaRepository:
    def __init__(self, turmaFactory: TurmaFactory):
        self.turmaFactory = turmaFactory
                
    def findTurmas(self) -> list[Turma]:
        response = supabase.table("turmas").select("*").execute()
        if response and response.data:
            data = response.data
            turmas = [self.turmaFactory.createTurma(turmas_dict) for turmas_dict in data]
            return turmas
        return []
    
    def findTurmasByDate(self, date: int) -> list[Turma]:
        response = supabase.table("turmas").select("*").eq("data_inicio", date).execute()
        if response and response.data:
            data = response.data
            turmas = [self.turmaFactory.createTurma(turmas_dict) for turmas_dict in data]
            return turmas
        return []
    
    def findTurmasPaginated(self, limit: int, page: int) -> tuple[list[Turma], int]:
        start = (page - 1) * limit
        end = start + limit - 1

        response = supabase.table("turmas").select("*", count='exact').range(start, end).execute()

        turmas = []
        total_turmas = 0

        if response and response.data:
            data = response.data
            turmas = [self.turmaFactory.createTurma(turmas_dict) for turmas_dict in data]
            total_turmas = response.count

        return turmas, total_turmas
    
    def findTurmaById(self, id_turma: int) -> Turma | None:
        response = supabase.table("turmas").select("*").eq("id_turma", id_turma).execute()
        if len(response.data) > 0:
            data = response.data[0]
            turma = self.turmaFactory.createTurma(data)
            return turma
        return None
    
    def saveTurma(self, turma: Turma) -> Turma|None:
        response = supabase.table("turmas").insert({
            "data_inicio": turma.data_inicio,
            "isgraduated": turma.isgraduated
            }).execute()
        
        if response.data:
            data = response.data[0]
            turma = self.turmaFactory.createTurma(data)
            return turma
        return None
    
    def saveTurmasFromCSV(self, turmas: list[Turma]) -> list[Turma]:
        turmas_dict = [turma.to_dict() for turma in turmas]

        response = supabase.table("turmas").insert(turmas_dict).execute()

        if response.data:
            data = response.data
            turmas = [self.turmaFactory.createTurma(turmas_dict) for turmas_dict in data]
            return turmas
        return []
    
    def deleteTurma(self, id_turma: int) -> Turma|None:
        supabase.table("turma_disciplina").delete().eq("id_turma", id_turma).execute()
        response = supabase.table("turmas").delete().eq("id_turma", id_turma).execute()

        if response.data:
            data = response.data[0]
            turma = self.turmaFactory.createTurma(data)
            return turma
        return None
    
    def updateTurma(self, turma: Turma) -> Turma|None:
        response = supabase.table("turmas").update({
                "data_inicio": turma.data_inicio,
                "isgraduated": turma.isgraduated
            }).eq("id_turma", turma.id_turma).execute()
        
        if response.data:
            data = response.data[0]
            turma = self.turmaFactory.createTurma(data)
            return turma
        return None
    
    def updateTurmaToGraduate(self, id_turma: int) -> Turma|None:
        response = supabase.table("turmas").update({
                "isgraduated": True
            }).eq("id_turma", id_turma).execute()
        
        if response.data:
            data = response.data[0]
            turma = self.turmaFactory.createTurma(data)
            return turma
        return None