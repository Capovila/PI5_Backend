from src.domain.Disciplina import Disciplina
from src.infrastructure.supabase_client import supabase


class DisciplinaRepository:
    def findDisciplinas(self) -> list[Disciplina]:
        response = supabase.table("disciplinas").select("*").execute()
        if response and response.data:
            data = response.data
            disciplinas = [
                Disciplina(
                    id_disciplina= disciplinas_dict["id_disciplina"],
                    nome= disciplinas_dict["nome"],
                    descricao= disciplinas_dict["descricao"],
                    semestre= disciplinas_dict["semestre"],
                    ra_professor= disciplinas_dict["ra_professor"],
                    dificuldade= disciplinas_dict["dificuldade"],
                )
                for disciplinas_dict in data
            ]
            return disciplinas
        return []
    
    def findDisciplinasBySemestre(self, semestre: int) -> list[Disciplina]:
        response = supabase.table("disciplinas").select("*").eq("semestre", semestre).execute()
        if response and response.data:
            data = response.data
            disciplinas = [
                Disciplina(
                    id_disciplina= disciplinas_dict["id_disciplina"],
                    nome= disciplinas_dict["nome"],
                    descricao= disciplinas_dict["descricao"],
                    semestre= disciplinas_dict["semestre"],
                    ra_professor= disciplinas_dict["ra_professor"],
                    dificuldade= disciplinas_dict["dificuldade"],
                )
                for disciplinas_dict in data
            ]
            return disciplinas
        return []
    
    """
    def findDisciplinasByArea(self, area_relacionada: str) -> list[Disciplina]:
        response = supabase.table("disciplinas").select("*").eq("area_relacionada", area_relacionada).execute()
        if response and response.data:
            data = response.data
            disciplinas = [
                Disciplina(
                    id_disciplina= disciplinas_dict["id_disciplina"],
                    nome= disciplinas_dict["nome"],
                    descricao= disciplinas_dict["descricao"],
                    semestre= disciplinas_dict["semestre"],
                    ra_professor= disciplinas_dict["ra_professor"],
                    dificuldade= disciplinas_dict["dificuldade"],
                )
                for disciplinas_dict in data
            ]
            return disciplinas
        return []
    """
    
    def findDisciplinasPaginated(self, limit: int, page: int) -> tuple[list[Disciplina], int]:
        start = (page - 1) * limit
        end = start + limit - 1

        response = supabase.table("disciplinas").select("*", count='exact').range(start, end).execute()

        disciplinas = []
        total_disciplinas = 0

        if response and response.data:
            data = response.data
            disciplinas = [
                Disciplina(
                    id_disciplina= disciplinas_dict["id_disciplina"],
                    nome= disciplinas_dict["nome"],
                    descricao= disciplinas_dict["descricao"],
                    semestre= disciplinas_dict["semestre"],
                    ra_professor= disciplinas_dict["ra_professor"],
                    dificuldade= disciplinas_dict["dificuldade"],
                )
                for disciplinas_dict in data
            ]
            total_disciplinas = response.count

        return disciplinas, total_disciplinas
    
    def findDisciplinaById(self, id_disciplina: int) -> Disciplina | None:
        response = supabase.table("disciplinas").select("*").eq("id_disciplina", id_disciplina).execute()
        if len(response.data) > 0:
            data = response.data[0]
            disciplina = Disciplina(
                id_disciplina=data["id_disciplina"],
                nome=data["nome"],
                descricao=data["descricao"],
                semestre=data["semestre"],
                ra_professor=data["ra_professor"],
                dificuldade=data["dificuldade"],
            )
            return disciplina
        return None
    
    def findDisciplinasByProfessorRa(self, ra_professor: int) -> list[Disciplina]:
        response = supabase.table("disciplinas").select("*").eq("ra_professor", ra_professor).execute()
        if response and response.data:
            data = response.data
            disciplinas = [
                Disciplina(
                    id_disciplina= disciplinas_dict["id_disciplina"],
                    nome= disciplinas_dict["nome"],
                    descricao= disciplinas_dict["descricao"],
                    semestre= disciplinas_dict["semestre"],
                    ra_professor= disciplinas_dict["ra_professor"],
                    dificuldade= disciplinas_dict["dificuldade"],
                )
                for disciplinas_dict in data
            ]
            return disciplinas
        return []
    
    def saveDisciplina(self, disciplina: Disciplina) -> Disciplina|None:
        response = supabase.table("disciplinas").insert({
                "nome": disciplina.nome,
                "descricao": disciplina.descricao,
                "dificuldade": disciplina.dificuldade,
                "semestre": disciplina.semestre,
                "ra_professor": disciplina.ra_professor
            }).execute()
        
        if response.data:
            data = response.data[0]
            return Disciplina(
                id_disciplina=data["id_disciplina"],
                nome=data["nome"],
                descricao=data["descricao"],
                semestre=data["semestre"],
                ra_professor=data["ra_professor"],
                dificuldade=data["dificuldade"]
            )
        return None
    
    def saveDisciplinasFromCSV(self, disciplinas: list[Disciplina]) -> list[Disciplina]:
        disciplinas_dict = [disciplina.to_dict() for disciplina in disciplinas]

        response = supabase.table("disciplinas").insert(disciplinas_dict).execute()

        if response.data:
            data = response.data
            disciplinas = [
                Disciplina(
                    id_disciplina= disciplinas_dict["id_disciplina"],
                    nome= disciplinas_dict["nome"],
                    descricao= disciplinas_dict["descricao"],
                    semestre= disciplinas_dict["semestre"],
                    ra_professor= disciplinas_dict["ra_professor"],
                    dificuldade= disciplinas_dict["dificuldade"],
                )
                for disciplinas_dict in data
            ]
            return disciplinas
        return []
    
    def deleteDisciplina(self, id_disciplina: int) -> Disciplina|None:
        response = supabase.table("disciplinas").delete().eq("id_disciplina", id_disciplina).execute()

        if response.data:
            data = response.data[0]
            disciplina = Disciplina(
                id_disciplina=data["id_disciplina"],
                nome=data["nome"],
                descricao=data["descricao"],
                semestre=data["semestre"],
                ra_professor=data["ra_professor"],
                dificuldade=data["dificuldade"]
            )
            return disciplina
        return None
    
    def updateDisciplina(self, disciplina: Disciplina) -> Disciplina|None:
        response = supabase.table("disciplinas").update({
                "nome": disciplina.nome,
                "descricao": disciplina.descricao,
                "dificuldade": disciplina.dificuldade,
                "semestre": disciplina.semestre,
                "ra_professor": disciplina.ra_professor
            }).eq("id_disciplina", disciplina.id_disciplina).execute()
        
        if response.data:
            data = response.data[0]
            disciplina = Disciplina(
                id_disciplina=data["id_disciplina"],
                nome=data["nome"],
                descricao=data["descricao"],
                semestre=data["semestre"],
                ra_professor=data["ra_professor"],
                dificuldade=data["dificuldade"]
            )
            return disciplina
        return None