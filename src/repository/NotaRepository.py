from src.domain.Nota import Nota
from src.infrastructure.supabase_client import supabase

class NotaRepository:
    def findNotas(self) -> list[Nota]:
        response = supabase.table("notas").select("*").execute()
        if response and response.data:
            data = response.data
            notas = [
                Nota(
                    id_notas=notas_dict["id_notas"],
                    ra_aluno=notas_dict["ra_aluno"],
                    id_disciplina=notas_dict["id_disciplina"],
                    nota=notas_dict["nota"]
                )
                for notas_dict in data
            ]
            return notas
        return []
    
    def findNotasPaginated(self, limit: int, page: int) -> tuple[list[Nota], int]:
        start = (page - 1) * limit
        end = start + limit - 1

        response = supabase.table("notas").select("*", count='exact').range(start, end).execute()

        notas = []
        total_notas = 0

        if response and response.data:
            data = response.data
            notas = [
                Nota(
                    id_notas=notas_dict["id_notas"],
                    ra_aluno=notas_dict["ra_aluno"],
                    id_disciplina=notas_dict["id_disciplina"],
                    nota=notas_dict["nota"]
                )
                for notas_dict in data
            ]
            total_notas = response.count

        return notas, total_notas
    
    def findNotaById(self, id: int) -> Nota | None:
        response = supabase.table("notas").select("*").eq("id_notas", id).execute()
        if len(response.data) > 0:
            data = response.data[0]
            nota = Nota(
                id_notas=data["id_notas"],
                ra_aluno=data["ra_aluno"],
                id_disciplina=data["id_disciplina"],
                nota=data["nota"]
            )
            return nota
        return None
    
    def findNotasByAlunoId(self, ra_aluno: int) -> list[Nota]:
        response = supabase.table("notas").select("*").eq("ra_aluno", ra_aluno).execute()
        if response and response.data:
            data = response.data
            notas = [
                Nota(
                    id_notas=notas_dict["id_notas"],
                    ra_aluno=notas_dict["ra_aluno"],
                    id_disciplina=notas_dict["id_disciplina"],
                    nota=notas_dict["nota"]
                )
                for notas_dict in data
            ]
            return notas
        return []
    
    def findNotasByDisciplinaId(self, id_disciplina: int) -> list[Nota]:
        response = supabase.table("notas").select("*").eq("id_disciplina", id_disciplina).execute()
        if response and response.data:
            data = response.data
            notas = [
                Nota(
                    id_notas=notas_dict["id_notas"],
                    ra_aluno=notas_dict["ra_aluno"],
                    id_disciplina=notas_dict["id_disciplina"],
                    nota=notas_dict["nota"]
                )
                for notas_dict in data
            ]
            return notas
        return []
    
    def saveNota(self, nota: Nota) -> Nota|None:
        response = supabase.table("notas").insert({
            "ra_aluno":nota.ra_aluno,
            "id_disciplina":nota.id_disciplina,
            "nota":nota.nota
            }).execute()
        
        if response.data:
            data = response.data[0]
            return Nota(
                id_notas=data["id_notas"],
                ra_aluno=data["ra_aluno"],
                id_disciplina=data["id_disciplina"],
                nota=data["nota"]
            )
        return None
    
    def saveNotasFromCSV(self, notas: list[Nota]) -> list[Nota]:
        notas_dict = [nota.to_dict() for nota in notas]

        response = supabase.table("notas").insert(notas_dict).execute()

        if response.data:
            data = response.data
            notas = [
                Nota(
                    ra_aluno=notas_dict["ra_aluno"],
                    id_disciplina=notas_dict["id_disciplina"],
                    nota=notas_dict["nota"]
                )
                for notas_dict in data
            ]
            return notas
        return []
    
    def deleteNota(self, id_notas: int) -> Nota|None:
        response = supabase.table("notas").delete().eq("id_notas", id_notas).execute()

        if response.data:
            data = response.data[0]
            nota = Nota(
                id_notas=data["id_notas"],
                ra_aluno=data["ra_aluno"],
                id_disciplina=data["id_disciplina"],
                nota=data["nota"]
            )
            return nota
        return None
    
    def updateNota(self, nota: Nota) -> Nota|None:
        response = supabase.table("notas").update({
                "ra_aluno": nota.ra_aluno,
                "id_disciplina":nota.id_disciplina,
                "nota": nota.nota
            }).eq("id_notas", nota.id_notas).execute()
        
        if response.data:
            data = response.data[0]
            nota = Nota(
                id_notas=data["id_notas"],
                ra_aluno=data["ra_aluno"],
                id_disciplina=data["id_disciplina"],
                nota=data["nota"]
            )
            return nota
        return None