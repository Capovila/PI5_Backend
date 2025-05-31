from src.domain.Turma import Turma
from src.infrastructure.supabase_client import supabase


class TurmaRepository:
    def findTurmas(self) -> list[Turma]:
        response = supabase.table("turmas").select("*").execute()
        if response and response.data:
            data = response.data
            turmas = [
                Turma(
                    id_turma= turmas_dict["id_turma"],
                    data_inicio= turmas_dict["data_inicio"],
                    isgraduated= turmas_dict["isgraduated"],
                )
                for turmas_dict in data
            ]
            return turmas
        return []
    
    def findTurmasByDate(self, date: int) -> list[Turma]:
        response = supabase.table("turmas").select("*").eq("data_inicio", date).execute()
        if response and response.data:
            data = response.data
            turmas = [
                Turma(
                    id_turma= turmas_dict["id_turma"],
                    data_inicio= turmas_dict["data_inicio"],
                    isgraduated= turmas_dict["isgraduated"],
                )
                for turmas_dict in data
            ]
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
            turmas = [
                Turma(
                    id_turma= turmas_dict["id_turma"],
                    data_inicio= turmas_dict["data_inicio"],
                    isgraduated= turmas_dict["isgraduated"],
                )
                for turmas_dict in data
            ]
            total_turmas = response.count

        return turmas, total_turmas
    
    def findTurmaById(self, id_turma: int) -> Turma | None:
        response = supabase.table("turmas").select("*").eq("id_turma", id_turma).execute()
        if len(response.data) > 0:
            data = response.data[0]
            turma = Turma(
                id_turma= data["id_turma"],
                data_inicio= data["data_inicio"],
                isgraduated= data["isgraduated"],
            )
            return turma
        return None
    
    def saveTurma(self, turma: Turma) -> Turma|None:
        response = supabase.table("turmas").insert({
            "data_inicio": turma.data_inicio,
            "isgraduated": turma.isgraduated
            }).execute()
        
        if response.data:
            data = response.data[0]
            return Turma(
                id_turma= data["id_turma"],
                data_inicio= data["data_inicio"],
                isgraduated= data["isgraduated"],
            )
        return None
    
    def saveTurmasFromCSV(self, turmas: list[Turma]) -> list[Turma]:
        turmas_dict = [turma.to_dict() for turma in turmas]

        response = supabase.table("turmas").insert(turmas_dict).execute()

        if response.data:
            data = response.data
            turmas = [
                Turma(
                    data_inicio= turmas_dict["data_inicio"],
                    isgraduated= turmas_dict["isgraduated"],
                )
                for turmas_dict in data
            ]
            return turmas
        return []
    
    def deleteTurma(self, id_turma: int) -> Turma|None:
        supabase.table("turma_disciplina").delete().eq("id_turma", id_turma).execute()
        response = supabase.table("turmas").delete().eq("id_turma", id_turma).execute()

        if response.data:
            data = response.data[0]
            turma = Turma(
                id_turma= data["id_turma"],
                data_inicio= data["data_inicio"],
                isgraduated= data["isgraduated"],
            )
            return turma
        return None
    
    def updateTurma(self, turma: Turma) -> Turma|None:
        response = supabase.table("turmas").update({
                "data_inicio": turma.data_inicio,
                "isgraduated": turma.isgraduated
            }).eq("id_turma", turma.id_turma).execute()
        
        if response.data:
            data = response.data[0]
            turma = Turma(
                id_turma= data["id_turma"],
                data_inicio= data["data_inicio"],
                isgraduated= data["isgraduated"],
            )
            return turma
        return None
    
    def updateTurmaToGraduate(self, id_turma: int) -> Turma|None:
        response = supabase.table("turmas").update({
                "isgraduated": True
            }).eq("id_turma", id_turma).execute()
        
        if response.data:
            data = response.data[0]
            turma = Turma(
                id_turma= data["id_turma"],
                data_inicio= data["data_inicio"],
                isgraduated= data["isgraduated"],
            )
            return turma
        return None