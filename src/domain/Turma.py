class Turma:
    def __init__(self, data_inicio:str, isgraduated:bool, id_turma:int = None):
        self.id_turma: int = id_turma
        self.data_inicio: str = data_inicio
        self.isgraduated: bool = isgraduated

    def to_dict(self):
        return {
            "id_turma": self.id_turma,
            "data_inicio": self.data_inicio,
            "isgraduated": self.isgraduated
        }