class TurmaDisciplina:
    def __init__(self, id_turma:int, id_disciplina:int, taxa_aprovacao:float, is_concluida:bool, id_turma_disciplina:int = None):
        self.id_turma_disciplina: int = id_turma_disciplina
        self.id_turma: int = id_turma
        self.id_disciplina: int = id_disciplina
        self.taxa_aprovacao: float = taxa_aprovacao
        self.is_concluida: bool = is_concluida

    def to_dict(self):
        return {
            "id_turma_disciplina": self.id_turma_disciplina,
            "id_turma": self.id_turma,
            "id_disciplina": self.id_disciplina,
            "taxa_aprovacao": self.taxa_aprovacao,
            "is_concluida": self.is_concluida
        }