from flask import Flask
from src.professores.professoresRoutes import professores_bp
from src.turmas.turmasRoutes import turmas_bp
from src.disciplinas.disciplinasRoutes import disciplinas_bp
from src.alunos.alunosRoutes import alunos_bp
from src.notas.notasRoutes import notas_bp
from src.turmaDisciplina.turmaDisciplinaRoutes import turma_disciplina_bp
import os
os.environ["WERKZEUG_DEBUG_PIN"] = "off"
app = Flask(__name__)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)
app.register_blueprint(disciplinas_bp)
app.register_blueprint(alunos_bp)
app.register_blueprint(notas_bp)
app.register_blueprint(turma_disciplina_bp)

@app.route("/", methods=["GET"])
def home():
    return "Hello world..."

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=3030, debug=True)
