import sys
import os

import pandas as pd
from flask import Blueprint, jsonify, request

from src.services.linearRegressionService import train_linear_regression

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from supabase_client import supabase

regression_model_bp = Blueprint("linearRegression", __name__, url_prefix="/linearRegression")

@regression_model_bp.route("/train_model", methods=["GET"])
def train_model():
    try:
        response = supabase.rpc('get_dataset').execute()
        data = response.data
        df = pd.DataFrame(data)
        train_linear_regression(df)
        return jsonify("Trained model successfully")
    except Exception as err:
        print(err)
        return jsonify({"error": "Erro ao puxar os dados"})