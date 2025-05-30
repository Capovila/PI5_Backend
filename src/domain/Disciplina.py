class Disciplina:
    def __init__(self, nome:str, descricao:str, semestre:int, ra_professor:int, dificuldade:int, id_disciplina:int = None):
        self.id_disciplina: int = id_disciplina
        self.nome: str = nome
        self.descricao: str = descricao
        self.semestre: int = semestre
        self.ra_professor: int = ra_professor
        self.dificuldade: int = dificuldade

    def to_dict(self):
        return {
            "id_disciplina": self.id_disciplina,
            "nome": self.nome,
            "descricao": self.descricao,
            "semestre": self.semestre,
            "ra_professor": self.ra_professor,
            "dificuldade": self.dificuldade
        }