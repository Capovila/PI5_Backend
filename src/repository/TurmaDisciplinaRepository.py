import traceback
from src.domain.TurmaDisciplina import TurmaDisciplina
from src.factories.TurmaDisciplina.TurmaDisciplinaFactory import TurmaDisciplinaFactory
from src.infrastructure.supabase_client import supabase


class TurmaDisciplinaRepository:
    def __init__(self, turmaDisciplinaFactory: TurmaDisciplinaFactory):
        self.turmaDisciplinaFactory = turmaDisciplinaFactory
        
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
            turmaDisciplinas = [self.turmaDisciplinaFactory.createTurmaDisciplina(turmaDisciplinas_dict) for turmaDisciplinas_dict in data]
            return turmaDisciplinas
        return []
    
    def findTurmaDisciplinaById(self, id_turma_disciplina: int) -> TurmaDisciplina | None:
        response = supabase.table("turma_disciplina").select("*").eq("id_turma_disciplina", id_turma_disciplina).execute()
        if len(response.data) > 0:
            data = response.data[0]
            turmaDisciplina = self.turmaDisciplinaFactory.createTurmaDisciplina(data)
            return turmaDisciplina
        return None
    
    def findTurmaDisciplinasByTurma(self, id_turma: str) -> list[TurmaDisciplina]:
        response = supabase.table("turma_disciplina").select("*, disciplinas(id_disciplina, nome, semestre, ra_professor)").eq("id_turma", id_turma).execute()
        if response and response.data:
            data = response.data
            turmaDisciplinas = [self.turmaDisciplinaFactory.createTurmaDisciplina(turmaDisciplinas_dict) for turmaDisciplinas_dict in data]
            return turmaDisciplinas
        return []
    
    def findTurmaDisciplinasByDisciplina(self, id_disciplina: int) -> list[TurmaDisciplina]:
        response = supabase.table("turma_disciplina").select("*").eq("id_disciplina", id_disciplina).execute()
        if response and response.data:
            data = response.data
            turmaDisciplinas = [self.turmaDisciplinaFactory.createTurmaDisciplina(turmaDisciplinas_dict) for turmaDisciplinas_dict in data]
            return turmaDisciplinas
        return []
    
    def findTurmaDisciplinasByProfessor(self, email: str) -> list[dict]:
        result = supabase.table("professores").select("ra_professor").eq("email", email).execute()
        if result and result.data:
            ra_professor = result.data[0]["ra_professor"]
            response = supabase.table("turma_disciplina").select(
                    "id_turma_disciplina, id_turma, id_disciplina, taxa_aprovacao, is_concluida, disciplinas(id_disciplina, nome, descricao, semestre, dificuldade, ra_professor)"
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
            turmaDisciplina = self.turmaDisciplinaFactory.createTurmaDisciplina(data)
            return turmaDisciplina
        return None
    
    def saveTurmaDisciplinasFromCSV(self, turmaDisciplinas: list[TurmaDisciplina]) -> list[TurmaDisciplina]:
        try:
            turmaDisciplinas_payload_list = [td.to_database_payload() for td in turmaDisciplinas]
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!! ERRO AO PREPARAR O PAYLOAD (to_database_payload) !!!")
            print(f"Tipo do Erro: {type(e)}")
            print(f"Mensagem do Erro: {str(e)}")
            print(f"Traceback Completo:\n{traceback.format_exc()}")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            raise

        print(f"Turma_Disciplinas a serem inseridas (objetos): {turmaDisciplinas}")
        print(f"PAYLOAD EXATO SENDO ENVIADO PARA O SUPABASE: {turmaDisciplinas_payload_list}")

        try:
            response = supabase.table("turma_disciplina").insert(turmaDisciplinas_payload_list).execute()
            print(f"Resposta do Supabase: {response}")
        except Exception as e: # Captura QUALQUER exceção durante a chamada ao Supabase
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"!!! ERRO DURANTE A INSERÇÃO NO SUPABASE (importar_csv) !!!")
            print(f"Tipo do Erro: {type(e)}")
            print(f"Mensagem do Erro: {str(e)}")
            print(f"Payload que foi enviado: {turmaDisciplinas_payload_list}") # Log do payload que falhou
            print(f"Traceback Completo:\n{traceback.format_exc()}")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            raise # Re-levanta a exceção para que o servidor ainda retorne 500

        if response and response.data:
            data = response.data
            turmasDisciplinas_criadas = []
            for turma_disciplina in data:
                turmasDisciplinas_criadas.append(
                    self.turmaDisciplinaFactory.createTurmaDisciplina(turma_disciplina)
                )
            print(f"Turma_Disciplinas inseridas com sucesso (objetos retornados): {turmasDisciplinas_criadas}")
            return turmasDisciplinas_criadas
        
        print("Nenhum dado retornado do Supabase após a inserção, ou a resposta não continha dados.")
        return []
    
    def deleteTurmaDisciplina(self, id_turma_disciplina: int) -> TurmaDisciplina|None:
        response = supabase.table("turma_disciplina").delete().eq("id_turma_disciplina", id_turma_disciplina).execute()

        if response.data:
            data = response.data[0]
            turmaDisciplina = self.turmaDisciplinaFactory.createTurmaDisciplina(data)
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
            turmaDisciplina = self.turmaDisciplinaFactory.createTurmaDisciplina(data)
            return turmaDisciplina
        return None
    
    def updateTurmaDisciplinaToConcluida(self, id_turma_disciplina: int) -> TurmaDisciplina|None:
        response = supabase.table("turma_disciplina").update({
                "is_concluida": True
            }).eq("id_turma_disciplina", id_turma_disciplina).execute()
        
        if response.data:
            data = response.data[0]
            turmaDisciplina = self.turmaDisciplinaFactory.createTurmaDisciplina(data)
            return turmaDisciplina
        return None