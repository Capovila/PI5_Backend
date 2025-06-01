class Professor:
    def __init__(self, ra_professor:int, nome:str, email:str, senha:str, is_admin:bool, is_liberado:bool):
        self.ra_professor: int = ra_professor
        self.nome: str = nome
        self.email: str = email
        self.senha: str = senha
        self.is_admin: bool = is_admin
        self.is_liberado: bool = is_liberado

    def to_dict(self):
        return {
            "ra_professor": self.ra_professor,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "is_admin": self.is_admin,
            "is_liberado": self.is_liberado
        }
    
    def to_database_payload(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "is_admin": self.is_admin,
            "is_liberado": self.is_liberado
        }
    
    