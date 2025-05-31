from src.domain.Professor import Professor
from src.infrastructure.supabase_client import supabase


class ProfessorRepository:
    def findProfessores(self) -> list[Professor]:
        response = supabase.table("professores").select("*").execute()
        if response and response.data:
            data = response.data
            professores = [
                Professor(
                    ra_professor= professores_dict["ra_professor"],
                    nome= professores_dict["nome"],
                    email= professores_dict["email"],
                    senha= professores_dict["senha"],
                    is_admin= professores_dict["is_admin"],
                    is_liberado= professores_dict["is_liberado"]
                )
                for professores_dict in data
            ]
            return professores
        return []
    
    def findProfessorById(self, ra_professor: int) -> Professor | None:
        response = supabase.table("professores").select("*").eq("ra_professor", ra_professor).execute()
        if len(response.data) > 0:
            data = response.data[0]
            professor = Professor(
                    ra_professor= data["ra_professor"],
                    nome= data["nome"],
                    email= data["email"],
                    senha= data["senha"],
                    is_admin= data["is_admin"],
                    is_liberado= data["is_liberado"]
            )
            return professor
        return None
    
    def findProfessoresPaginated(self, limit: int, page: int) -> tuple[list[Professor], int]:
        start = (page - 1) * limit
        end = start + limit - 1

        response = supabase.table("professores").select("*", count='exact').range(start, end).execute()

        professores = []
        total_professores = 0

        if response and response.data:
            data = response.data
            professores = [
                Professor(
                    ra_professor= professores_dict["ra_professor"],
                    nome= professores_dict["nome"],
                    email= professores_dict["email"],
                    senha= professores_dict["senha"],
                    is_admin= professores_dict["is_admin"],
                    is_liberado= professores_dict["is_liberado"]
                )
                for professores_dict in data
            ]
            total_professores = response.count

        return professores, total_professores
    
    def saveProfessor(self, professor: Professor) -> Professor|None:
        response = supabase.table("professores").insert({
                "ra_professor": professor.ra_professor,
                "nome": professor.nome,
                "email": professor.email,
                "senha": professor.senha,
                "is_admin": professor.is_admin,
                "is_liberado": professor.is_liberado
            }).execute()
        
        if response.data:
            data = response.data[0]
            return Professor(
                ra_professor= data["ra_professor"],
                nome= data["nome"],
                email= data["email"],
                senha= data["senha"],
                is_admin= data["is_admin"],
                is_liberado= data["is_liberado"]
            )
        return None
    
    def saveProfessoresFromCSV(self, professores: list[Professor]) -> list[Professor]:
        professores_dict = [professore.to_dict() for professore in professores]

        response = supabase.table("professores").insert(professores_dict).execute()

        if response.data:
            data = response.data
            professores = [
                Professor(
                    ra_professor= professores_dict["ra_professor"],
                    nome= professores_dict["nome"],
                    email= professores_dict["email"],
                    senha= professores_dict["senha"],
                    is_admin= professores_dict["is_admin"],
                    is_liberado= professores_dict["is_liberado"]
                )
                for professores_dict in data
            ]
            return professores
        return []
    
    def deleteProfessor(self, ra_professor: int) -> Professor|None:
        response = supabase.table("professores").delete().eq("ra_professor", ra_professor).execute()

        if response.data:
            data = response.data[0]
            professor = Professor(
                ra_professor= data["ra_professor"],
                nome= data["nome"],
                email= data["email"],
                senha= data["senha"],
                is_admin= data["is_admin"],
                is_liberado= data["is_liberado"]
            )
            return professor
        return None
    
    def updateProfessor(self, professor: Professor) -> Professor|None:
        response = supabase.table("professores").update({
                "nome": professor.nome,
                "email": professor.email,
                "senha": professor.senha,
                "is_admin": professor.is_admin,
                "is_liberado": professor.is_liberado
            }).eq("ra_professor", professor.ra_professor).execute()
        
        if response.data:
            data = response.data[0]
            professor = Professor(
                ra_professor= data["ra_professor"],
                nome= data["nome"],
                email= data["email"],
                senha= data["senha"],
                is_admin= data["is_admin"],
                is_liberado= data["is_liberado"]
            )
            return professor
        return None
    
    def updateProfessorToAdmin(self, ra_professor: int) -> Professor|None:

        current_status = supabase.table("professores").select("is_admin").eq("ra_professor", ra_professor).execute()
        
        new_status = not current_status.data[0]["is_admin"]
        
        response = supabase.table("professores").update({
                "is_admin": new_status
            }).eq("ra_professor", ra_professor).execute()
        
        if response.data:
            data = response.data[0]
            professor = Professor(
                ra_professor= data["ra_professor"],
                nome= data["nome"],
                email= data["email"],
                senha= data["senha"],
                is_admin= data["is_admin"],
                is_liberado= data["is_liberado"]
            )
            return professor
        return None
    
    def liberarProfessor(self, ra_professor: int) -> Professor|None:
        response = supabase.table("professores").update({
                "is_liberado": True
            }).eq("ra_professor", ra_professor).execute()
        
        if response.data:
            data = response.data[0]
            professor = Professor(
                ra_professor= data["ra_professor"],
                nome= data["nome"],
                email= data["email"],
                senha= data["senha"],
                is_admin= data["is_admin"],
                is_liberado= data["is_liberado"]
            )
            return professor
        return None