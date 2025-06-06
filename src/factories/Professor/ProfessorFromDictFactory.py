from src.domain.Professor import Professor
from .ProfessorFactory import ProfessorFactory

class ProfessorFromDictFactory(ProfessorFactory):
    def createProfessor(self, data: dict) -> Professor:
        return Professor(
            ra_professor=data["ra_professor"],
            nome=data["nome"],
            email=data["email"],
            senha=data["senha"],
            is_admin=data["is_admin"],
            is_liberado=data["is_liberado"]
        )
