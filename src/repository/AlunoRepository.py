from src.domain.Aluno import Aluno
from src.infrastructure.supabase_client import supabase


class AlunoRepository:
    def findAlunos(self) -> list[Aluno]:
        response = supabase.table("alunos").select("*").execute()
        if response and response.data:
            data = response.data
            alunos = [
                Aluno(
                    ra_aluno=alunos_dict["ra_aluno"],
                    nome=alunos_dict["nome"],
                    id_turma=alunos_dict["id_turma"],
                )
                for alunos_dict in data
            ]
            return alunos
        return []

    def findAlunoByRaAluno(self, ra_aluno: int) -> Aluno|None:
        response = supabase.table("alunos").select("*").eq("ra_aluno", ra_aluno).execute()
        if len(response.data) > 0:
            data = response.data[0]
            aluno = Aluno(
                ra_aluno=data["ra_aluno"],
                nome=data["nome"],
                id_turma=data["id_turma"],
            )
            return aluno
        return None

    def findAlunosPaginated(self, limit: int, page: int) -> tuple[list[Aluno], int]:
        start = (page - 1) * limit
        end = start + limit - 1

        response = supabase.table("alunos").select("*", count='exact').range(start, end).execute()

        alunos = []
        total_alunos = 0

        if response and response.data:
            data = response.data
            alunos = [
                Aluno(
                    ra_aluno=alunos_dict["ra_aluno"],
                    nome=alunos_dict["nome"],
                    id_turma=alunos_dict["id_turma"],
                )
                for alunos_dict in data
            ]
            total_alunos = response.count

        return alunos, total_alunos

    def findAlunosByTurma(self, id_turma: int) -> list[Aluno]:
        response = supabase.table("alunos").select("*").eq("id_turma", id_turma).execute()
        if response and response.data:
            data = response.data
            alunos = [
                Aluno(
                    ra_aluno=alunos_dict["ra_aluno"],
                    nome=alunos_dict["nome"],
                    id_turma=alunos_dict["id_turma"],
                )
                for alunos_dict in data
            ]
            return alunos
        return []

    def saveAluno(self, aluno: Aluno) -> Aluno|None:
        response = supabase.table("alunos").insert({
            "ra_aluno": aluno.ra_aluno,
            "nome": aluno.nome,
            "id_turma": aluno.id_turma
        }).execute()

        if response.data:
            data = response.data[0]
            return Aluno (
                ra_aluno=data["ra_aluno"],
                nome=data["nome"],
                id_turma=data["id_turma"],
            )
        return None

    def saveAlunosFromCSV(self, alunos: list[Aluno]) -> list[Aluno]:
        alunos_dict = [aluno.to_dict() for aluno in alunos]

        response = supabase.table("alunos").insert(alunos_dict).execute()

        if response.data:
            data = response.data
            alunos = [
                Aluno(
                    ra_aluno=alunos_dict["ra_aluno"],
                    nome=alunos_dict["nome"],
                    id_turma=alunos_dict["id_turma"],
                )
                for alunos_dict in data
            ]
            return alunos
        return []

    def deleteAluno(self, ra_aluno: int) -> Aluno|None:
        response = supabase.table("alunos").delete().eq("ra_aluno", ra_aluno).execute()

        if response.data:
            data = response.data[0]
            aluno = Aluno(
                ra_aluno=data["ra_aluno"],
                nome=data["nome"],
                id_turma=data["id_turma"],
            )
            return aluno
        return None

    def updateAluno(self, ra_aluno: int, nome: str, id_turma: int) -> Aluno|None:
        response = supabase.table("alunos").update({
            "nome": nome,
            "id_turma": id_turma
        }).eq("ra_aluno", ra_aluno).execute()

        if response.data:
            data = response.data[0]
            aluno = Aluno(
                ra_aluno=data["ra_aluno"],
                nome=data["nome"],
                id_turma=data["id_turma"],
            )
            return aluno
        return None
