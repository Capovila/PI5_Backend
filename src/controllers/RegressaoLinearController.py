import sys
import os

import pandas as pd
from flask import Blueprint, jsonify

from src.services.linearRegressionService import train_linear_regression

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.infrastructure.supabase_client import supabase

class RegressaoLinearController:
    def __init__(self):
        self.regressao_linear_bp = Blueprint("regressaoLinear", __name__, url_prefix="/regressaoLinear")
        self._register_routes()

    def _register_routes(self):
        self.regressao_linear_bp.route("/treinar_modelo", methods=["GET"])(self.train_model)

    def train_model(self):
        try:
            response = supabase.rpc('get_dataset').execute()
            data = response.data
            df = pd.DataFrame(data)
            train_linear_regression(df)
            return jsonify("Trained model successfully")
        except Exception as err:
            print(err)
            return jsonify({"error": "Erro ao puxar os dados"})