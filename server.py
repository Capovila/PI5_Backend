from flask import Flask
from professores.professoresRoutes import professores_bp
from turmas.turmasRoutes import turmas_bp
import os
os.environ["WERKZEUG_DEBUG_PIN"] = "off"
app = Flask(__name__)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)


@app.route("/", methods=["GET"])
def home():
    return "Hello world..."

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=3030, debug=True)
