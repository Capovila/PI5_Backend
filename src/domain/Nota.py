class Nota:
    def __init__(self, ra_aluno:int, id_disciplina:int, nota:int, id_notas:int = None):
        self.id_notas: int = id_notas
        self.ra_aluno: int = ra_aluno
        self.id_disciplina: int = id_disciplina
        self.nota: int = nota

    def to_dict(self):
        return {
            "id_notas": self.id_notas,
            "ra_aluno": self.ra_aluno,
            "id_disciplina": self.id_disciplina,
            "nota": self.nota
        }
    
    def to_database_payload(self):
        return {
            "ra_aluno": self.ra_aluno,
            "id_disciplina": self.id_disciplina,
            "nota": self.nota
        }