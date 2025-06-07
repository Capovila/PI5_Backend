from src.factories.Nota.NotaFactory import NotaFactory
from src.domain.Nota import Nota
from src.infrastructure.supabase_client import supabase

class NotaRepository:
    def __init__(self, notaFactory: NotaFactory):
        self.notaFactory = notaFactory
        
    def findNotas(self) -> list[Nota]:
        response = supabase.table("notas").select("*").execute()
        if response and response.data:
            data = response.data
            notas = [self.notaFactory.createNota(notas_dict) for notas_dict in data]
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
            notas = [self.notaFactory.createNota(notas_dict) for notas_dict in data]
            total_notas = response.count

        return notas, total_notas
    
    def findNotaById(self, id: int) -> Nota | None:
        response = supabase.table("notas").select("*").eq("id_notas", id).execute()
        if len(response.data) > 0:
            data = response.data[0]
            nota = self.notaFactory.createNota(data)
            return nota
        return None
    
    def findNotasByAlunoId(self, ra_aluno: int) -> list[Nota]:
        response = supabase.table("notas").select("*").eq("ra_aluno", ra_aluno).execute()
        if response and response.data:
            data = response.data
            notas = [self.notaFactory.createNota(notas_dict) for notas_dict in data]
            return notas
        return []
    
    def findNotasByDisciplinaId(self, id_disciplina: int) -> list[Nota]:
        response = supabase.table("notas").select("*").eq("id_disciplina", id_disciplina).execute()
        if response and response.data:
            data = response.data
            notas = [self.notaFactory.createNota(notas_dict) for notas_dict in data]
            return notas
        return []
    
    def findNotasByAlunoIdAndDisciplinaId(self, id_aluno: int, id_disciplina: int) -> list[Nota]:
        response = supabase.table("notas").select("*").eq("ra_aluno", id_aluno).eq("id_disciplina", id_disciplina).execute()
        if response and response.data:
            data = response.data
            notas = [self.notaFactory.createNota(notas_dict) for notas_dict in data]
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
            nota = self.notaFactory.createNota(data)
            return nota
        return None
    
    def saveNotasFromCSV(self, notas: list[Nota]) -> list[Nota]:
        notas_dict = [nota.to_dict() for nota in notas]
        for nota in notas_dict:
            nota.pop('id_notas', None)
            
        response = supabase.table("notas").insert(notas_dict).execute()
        if response and response.data:
            data = response.data
            notas = [self.notaFactory.createNota(nota_dict) for nota_dict in data]
            return notas
        return []
    
    def deleteNota(self, id_notas: int) -> Nota|None:
        response = supabase.table("notas").delete().eq("id_notas", id_notas).execute()

        if response.data:
            data = response.data[0]
            nota = self.notaFactory.createNota(data)
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
            nota = self.notaFactory.createNota(data)
            return nota
        return None