from src.domain.TurmaDisciplina import TurmaDisciplina
from src.infrastructure.supabase_client import supabase


class TurmaDisciplinaRepository:
    def findTurmaDisciplinas(self) -> list[TurmaDisciplina]:
        response = (
                supabase.table("turma_disciplina")
                .select(
                    "id_turma_disciplina, id_turma, id_disciplina, taxa_aprovacao, is_concluida"
                )
                .execute()
            )
        if response and response.data:
            data = response.data
            turmaDisciplinas = [
                TurmaDisciplina(
                    id_turma_disciplina= turmaDisciplinas_dict["id_turma_disciplina"],
                    id_turma= turmaDisciplinas_dict["id_turma"],
                    id_disciplina= turmaDisciplinas_dict["id_disciplina"],
                    taxa_aprovacao= turmaDisciplinas_dict["taxa_aprovacao"],
                    is_concluida= turmaDisciplinas_dict["is_concluida"]
                )
                for turmaDisciplinas_dict in data
            ]
            return turmaDisciplinas
        return []
    
    def findTurmaDisciplinaById(self, id_turma_disciplina: int) -> TurmaDisciplina | None:
        response = supabase.table("turma_disciplina").select("*").eq("id_turma_disciplina", id_turma_disciplina).execute()
        if len(response.data) > 0:
            data = response.data[0]
            turmaDisciplina = TurmaDisciplina(
                id_turma_disciplina= data["id_turma_disciplina"],
                id_turma= data["id_turma"],
                id_disciplina= data["id_disciplina"],
                taxa_aprovacao= data["taxa_aprovacao"],
                is_concluida= data["is_concluida"]
            )
            return turmaDisciplina
        return None
    
    def findTurmaDisciplinasByTurma(self, id_turma: str) -> list[TurmaDisciplina]:
        response = supabase.table("turma_disciplina").select("*").eq("id_turma", id_turma).execute()
        if response and response.data:
            data = response.data
            turmaDisciplina = [
                TurmaDisciplina(
                    id_turma_disciplina= turmaDisciplinas_dict["id_turma_disciplina"],
                    id_turma= turmaDisciplinas_dict["id_turma"],
                    id_disciplina= turmaDisciplinas_dict["id_disciplina"],
                    taxa_aprovacao= turmaDisciplinas_dict["taxa_aprovacao"],
                    is_concluida= turmaDisciplinas_dict["is_concluida"]
                )
                for turmaDisciplinas_dict in data
            ]
            return turmaDisciplina
        return []
    
    def findTurmaDisciplinasByDisciplina(self, id_disciplina: int) -> list[TurmaDisciplina]:
        response = supabase.table("turma_disciplina").select("*").eq("id_disciplina", id_disciplina).execute()
        if response and response.data:
            data = response.data
            turmaDisciplina = [
                TurmaDisciplina(
                    id_turma_disciplina= turmaDisciplinas_dict["id_turma_disciplina"],
                    id_turma= turmaDisciplinas_dict["id_turma"],
                    id_disciplina= turmaDisciplinas_dict["id_disciplina"],
                    taxa_aprovacao= turmaDisciplinas_dict["taxa_aprovacao"],
                    is_concluida= turmaDisciplinas_dict["is_concluida"]
                )
                for turmaDisciplinas_dict in data
            ]
            return turmaDisciplina
        return []
    
    def findTurmaDisciplinasByProfessor(self, email: str) -> list[dict]:
        result = supabase.table("professores").select("ra_professor").eq("email", email).execute()
        if result and result.data:
            ra_professor = result.data[0]["ra_professor"]
            response = supabase.table("turma_disciplina").select(
                    "id_turma_disciplina, id_turma, id_disciplina, taxa_aprovacao, is_concluida, disciplinas(id_disciplina, nome, descricao, semestre, area_relacionada, ra_professor)"
                ).execute()
            if response and response.data:
                data = response.data
                filtered_data = [
                    item for item in data
                    if item["disciplinas"] is not None and item["disciplinas"]["ra_professor"] == ra_professor
                ]
                return filtered_data
        return []
    
    def saveTurmaDisciplina(self, turmaDisciplina: TurmaDisciplina) -> TurmaDisciplina|None:
        response = supabase.table("turma_disciplina").insert({
                "id_turma": turmaDisciplina.id_turma,
                "id_disciplina": turmaDisciplina.id_disciplina,
                "taxa_aprovacao": turmaDisciplina.taxa_aprovacao if turmaDisciplina.is_concluida else None,
                "is_concluida": turmaDisciplina.is_concluida
            }).execute()
        
        if response.data:
            data = response.data[0]
            return TurmaDisciplina(
                id_turma_disciplina= data["id_turma_disciplina"],
                id_turma= data["id_turma"],
                id_disciplina= data["id_disciplina"],
                taxa_aprovacao= data["taxa_aprovacao"],
                is_concluida= data["is_concluida"]
            )
        return None
    
    def saveTurmaDisciplinasFromCSV(self, turmaDisciplinas: list[TurmaDisciplina]) -> list[TurmaDisciplina]:
        turmaDisciplinas_dict = [turmaDisciplina.to_dict() for turmaDisciplina in turmaDisciplinas]

        response = supabase.table("turma_disciplina").insert(turmaDisciplinas_dict).execute()

        if response.data:
            data = response.data
            turmaDisciplinas = [
                TurmaDisciplina(
                    id_turma_disciplina= turmaDisciplinas_dict["id_turma_disciplina"],
                    id_turma= turmaDisciplinas_dict["id_turma"],
                    id_disciplina= turmaDisciplinas_dict["id_disciplina"],
                    taxa_aprovacao= turmaDisciplinas_dict["taxa_aprovacao"],
                    is_concluida= turmaDisciplinas_dict["is_concluida"]
                )
                for turmaDisciplinas_dict in data
            ]
            return turmaDisciplinas
        return []
    
    def deleteTurmaDisciplina(self, id_turma_disciplina: int) -> TurmaDisciplina|None:
        response = supabase.table("turma_disciplina").delete().eq("id_turma_disciplina", id_turma_disciplina).execute()

        if response.data:
            data = response.data[0]
            turmaDisciplina = TurmaDisciplina(
                id_turma_disciplina= data["id_turma_disciplina"],
                id_turma= data["id_turma"],
                id_disciplina= data["id_disciplina"],
                taxa_aprovacao= data["taxa_aprovacao"],
                is_concluida= data["is_concluida"]
            )
            return turmaDisciplina
        return None
    
    def updateTurmaDisciplina(self, turmaDisciplina: TurmaDisciplina) -> TurmaDisciplina|None:
        response = supabase.table("turma_disciplina").update({
                "id_turma": turmaDisciplina.id_turma,
                "id_disciplina": turmaDisciplina.id_disciplina,
                "taxa_aprovacao": turmaDisciplina.taxa_aprovacao if turmaDisciplina.is_concluida else None,
                "is_concluida": turmaDisciplina.is_concluida
            }).eq("id_turma_disciplina", turmaDisciplina.id_turma_disciplina).execute()
        
        if response.data:
            data = response.data[0]
            turmaDisciplina = TurmaDisciplina(
                id_turma_disciplina= data["id_turma_disciplina"],
                id_turma= data["id_turma"],
                id_disciplina= data["id_disciplina"],
                taxa_aprovacao= data["taxa_aprovacao"],
                is_concluida= data["is_concluida"]
            )
            return turmaDisciplina
        return None
    
    def updateTurmaDisciplinaToConcluida(self, id_turma_disciplina: int) -> TurmaDisciplina|None:
        response = supabase.table("turma_disciplina").update({
                "is_concluida": True
            }).eq("id_turma_disciplina", id_turma_disciplina).execute()
        
        if response.data:
            data = response.data[0]
            turmaDisciplina = TurmaDisciplina(
                id_turma_disciplina= data["id_turma_disciplina"],
                id_turma= data["id_turma"],
                id_disciplina= data["id_disciplina"],
                taxa_aprovacao= data["taxa_aprovacao"],
                is_concluida= data["is_concluida"]
            )
            return turmaDisciplina
        return None