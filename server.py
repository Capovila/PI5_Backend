from flask import Flask
from flask_cors import CORS

from src.controllers.AlunoController import AlunoController
from src.controllers.DisciplinaController import DisciplinaController
from src.controllers.NotaController import NotaController
from src.controllers.ProfessorController import ProfessorController
from src.controllers.RegressaoLinearController import RegressaoLinearController
from src.turmas.turmasRoutes import turmas_bp
from src.turmaDisciplina.turmaDisciplinaRoutes import turma_disciplina_bp
import os
os.environ["WERKZEUG_DEBUG_PIN"] = "off"
app = Flask(__name__)
CORS(app)

alunoController = AlunoController()
disciplinaController = DisciplinaController()
regressaoLinearController = RegressaoLinearController()
notaController = NotaController()
professorController = ProfessorController()
app.register_blueprint(turmas_bp)
app.register_blueprint(alunoController.alunos_bp)
app.register_blueprint(disciplinaController.disciplinas_bp)
app.register_blueprint(regressaoLinearController.regressao_linear_bp)
app.register_blueprint(notaController.notas_bp)
app.register_blueprint(professorController.professores_bp)
app.register_blueprint(turma_disciplina_bp)

@app.route("/", methods=["GET"])
def home():
    return "Hello world..."

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=3030, debug=True)
