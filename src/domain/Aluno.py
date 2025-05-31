class Aluno:
    def __init__(self, ra_aluno:int, nome:str, id_turma: int):
        self.ra_aluno: int = ra_aluno
        self.nome: str = nome
        self.id_turma: int = id_turma

    def to_dict(self):
        return {
            "ra_aluno": self.ra_aluno,
            "nome": self.nome,
            "id_turma": self.id_turma,
        }